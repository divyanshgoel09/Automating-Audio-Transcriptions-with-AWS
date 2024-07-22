import json
import time   #imported to give jobs unique name 
import boto3

mytranscribe = boto3.client("transcribe", #service name 
                region_name="ap-south-1", #region name 
                )                         #we can give our aws_access_key_id and aws_secret_access_key here (it is hardcoded)
                                          #or we can also set both the keys in environment variabke (it is a better thing to do)

def lambda_handler(event, context):
    
    bucketName = event['Records'][0]['s3']['bucket']['name']
    
    fileName = event['Records'][0]['s3']['object']['key']
    
    #here we are utilizing lambda_handler event variable as it gets all the info about the events that happened when it get triggered 
    #we are using the info to find out or BUCKET NAME and FILENAME and generating a Final URL which is useful to get info of Uploaded file in Transcribe JOB
    
    finalURL = "s3://" + bucketName + "/" + fileName
    
    print (finalURL)
    
    response = mytranscribe.start_transcription_job(    #function provided by AWS can check in Documentation
            TranscriptionJobName= "my_transcription_job_" + str(int(time.time())),   #here we used the time to give make job name unique everytime
            LanguageCode='en-US',
            MediaFormat='mp3',
            Media={
                'MediaFileUri' : finalURL
            },
            OutputBucketName="project-s3-lambda-transcribe-output",
            OutputKey=fileName + "-" + "TextFile" + "-" + ".json" 
        ) 
        
    print(response)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
