from datetime import datetime 
import json
import uuid
import boto3

def lambda_handler(event, context):
    s3bucket = 'Your-Bucket-Name' ## ADD YOUR BUCKET NAME HERE ##
    try:
        s3 = boto3.resource('s3')
        s3.Object(s3bucket, str(uuid.uuid4())).put(
            Body=json.dumps(event, indent=2))
        return 'Event stored'
    except:
        raise

def random_string(event, timestamp):  
   
    def lambda_handler(event, context):
                        
        timestamp_format = "%Y/%m/%d/%H/%Y-%m-%d-%H-%M-%S-%f"
    
    if type(event) == type({}):
                if 'Sns' in record:
                    timestamp = datetime.datetime.now()
                    time_received = record['Sns']['Timestamp'] if 'Timestamp' in  record['Sns'] else None
                    if time_received: 
                        try:
                            timestamp = datetime.datetime.strptime(time_received, timestamp_format)
                        except: pass 
                    if 'Message' in record['Sns']:
                        Sns_messages = json.loads(record['Sns']['Message'])

    else:
    
        print("Received event: " + json.dumps(event, indent=2))
        
    return True
