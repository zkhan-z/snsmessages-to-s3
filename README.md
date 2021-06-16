# snsmessages-to-s3
Sending Sns messages to s3bucket by creating lambda function

## Create an Sns Topic
## Create s3Bucket and add permissoin for PutObject permission to allow SnsMessages to be forwarded to your bucket
## Create a Lambda function and add your code
## Add trigger to your lambda function pointing to your SnsTopic 

This repo will help you forward Sns notifications to s3bucket for storage. For this to work your lambda function needs Snstopic trigger and once invoked it will redirect these messages and upload them to an s3bucket that you created and output the information in a json format.
