# snsmessages-to-s3
This repo will help you forward Sns messages to s3bucket for storage and log analysis. For this to work your lambda function needs Sns trigger and once invoked it will redirect these messages and upload them to an s3bucket that you created and output the information in a json format. This is useful when using sns messages you would want to store.

Steps to execute:

-> Create an Sns Topic.
-> Create s3Bucket.
-> Create a Lambda function and add your code. Make sure your Lambda function has the required permissions to execute the code.
-> Add subscription for Sns Topic.
-> Add trigger to your lambda function pointing to your SnsTopic.
