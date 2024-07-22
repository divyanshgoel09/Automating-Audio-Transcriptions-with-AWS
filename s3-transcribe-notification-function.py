import json
import boto3

sns = boto3.client("sns", region_name="ap-south-1")

# Replace this with your SNS topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:654654630405:Transcribe-Notification'

def lambda_handler(event, context):
    # Get the output file details
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    message = f"Transcription job complete. Output file available at s3://{bucket_name}/{file_name}"
    
    # Publish to SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject='Transcription Job Completed'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent.')
    }
