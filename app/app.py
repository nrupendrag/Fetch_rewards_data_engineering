import boto3
import json
import hashlib
import psycopg2
import os

# Set AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = 'dummy'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

# Function to mask PII data and ensure all required keys are present
def mask_pii(data):
    data['masked_device_id'] = hashlib.sha256(data.get('device_id', 'default_device_id').encode()).hexdigest()
    data['masked_ip'] = hashlib.sha256(data.get('ip', '0.0.0.0').encode()).hexdigest()
    data['user_id'] = data.get('user_id', 'default_user_id')
    data['device_type'] = data.get('device_type', 'default_device_type')
    data['locale'] = data.get('locale', 'default_locale')

    # Convert app_version to an integer if possible, otherwise set to 0
    try:
        data['app_version'] = int(float(data.get('app_version', 0)))
    except ValueError:
        data['app_version'] = 0

    data['create_date'] = data.get('create_date', '1970-01-01')
    return data

# Function to insert data into PostgreSQL
def insert_into_db(data):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (
        data['user_id'], data['device_type'], data['masked_ip'], data['masked_device_id'],
        data['locale'], data['app_version'], data['create_date']
    ))
    conn.commit()
    cursor.close()
    conn.close()

# Function to receive messages from SQS
def receive_messages(queue_url):
    sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10
    )
    return response.get('Messages', [])

if __name__ == '__main__':
    queue_url = 'http://localhost:4566/000000000000/login-queue'
    messages = receive_messages(queue_url)
    for message in messages:
        data = json.loads(message['Body'])
        masked_data = mask_pii(data)
        insert_into_db(masked_data)
        print("Data inserted:", masked_data)
