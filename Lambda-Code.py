"""
Project : AWS Lambda S3 Upload Notification
Author  : Ashish J Talekar

Description:
This AWS Lambda function is triggered whenever a new file is uploaded
to an Amazon S3 bucket. It retrieves the bucket name and object name
from the S3 event and sends an email notification using Amazon SNS.

import boto3
import os

# Create SNS client
sns = boto3.client("sns")

# Read SNS Topic ARN from Environment Variable
TOPIC_ARN = os.environ["aws1"]


def lambda_handler(event, context):
    # Get S3 event details
    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    filename = record["s3"]["object"]["key"]

    # Create notification message
    message = f"""
A new file has been uploaded.

Bucket Name: {bucket}
File Name: {filename}
"""

    # Publish notification to Amazon SNS
    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="New File Uploaded",
        Message=message
    )

    # Return success response
    return {
        "statusCode": 200,
        "body": "Notification sent successfully."
    }
