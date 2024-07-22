# Automating-Audio-Transcriptions-with-AWS
### **Project Description:**
This project aims to build an automated system for processing audio files in AWS to generate text transcriptions using the AWS Transcribe Service. The objective is to automate the workflow so that when an audio file is uploaded to an S3 bucket, AWS Lambda triggers the transcription process, generating a text file. The resulting text file is then stored in a designated S3 bucket. Additionally, the system keeps stakeholders informed by sending an email notification via AWS SNS upon successful generation of the transcription file.

### **Key Features:**
1. Automated Transcription: AWS Transcribe efficiently converts speech to text with high accuracy, accommodating a wide range of formats and languages.
2. Seamless Integration: AWS Lambda automates the entire transcription workflow, ensuring that transcription jobs are executed and completed without manual intervention.
3. Real-Time Notifications: AWS SNS provides timely email notifications to users upon the completion of transcription, keeping them informed of the process status.
4. Scalability: The system is designed to handle multiple transcription jobs concurrently, making it well-suited for organizations of all sizes.
5. Secure Storage: Both input audio files and generated text files are securely managed and stored in AWS S3, ensuring data protection and integrity.

## **Overview:**
![TRANSCRIBE DIAGRAM-Page-2 (1)](https://github.com/user-attachments/assets/3c474d2d-1270-44ab-bbe3-c67931b94a66)

Created Two S3 Buckets
![image](https://github.com/user-attachments/assets/13a7b7ab-610c-4406-b816-340e4d7f9f64)

Create two LAMBDA Function
![image](https://github.com/user-attachments/assets/0b8d2a2f-b9c5-4116-80ba-46d20e324680)
Use the python code provided in python code files.


It triggers **s3-transcribe-function** Lambda function 
![image](https://github.com/user-attachments/assets/56e45feb-5632-434b-b4e6-1802275bc036)
We give certain Permissions to our Lambda Function by attaching certain policies to it.

Uploaded audio file in Input Bucket
![image](https://github.com/user-attachments/assets/4aff7d18-6921-449e-8997-94b2e9a5e2be)

Lambda Function starts our Transcribe Job

Now our Output File get generated and store in Output S3 bucket
![image](https://github.com/user-attachments/assets/f4b34151-b5d3-4c97-a67d-33353f6af088)

Now our **s3-transcribe-notification-function** gets triggered 
![image](https://github.com/user-attachments/assets/891f6490-fb39-40d9-85de-9d140c621874)

Now the user receives notification about Transcription job completion
![image](https://github.com/user-attachments/assets/e40562ba-8b4d-4d44-a317-e329d7fcd8d3)

