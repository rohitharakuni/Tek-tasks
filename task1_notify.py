#Create AWS lambda script to verify and generate email.

#1)A lambda that notifies users who have not logged in to the console for 2 months and  that their console access is about to be removed
#(Warning mail).They should get another reminder at the 3 months.
#2)lambda code is to be written in Python/shell/or any scripting language.


import boto3
from datetime import datetime, timezone
import json

# Connect to the AWS IAM service
iam = boto3.client('iam')

# Connect to the AWS SNS service
sns = boto3.client('sns')

def lambda_handler(event, context):
    # Get the list of IAM users
    users = iam.list_users()['Users']
    
    # Get the current date
    current_date = datetime.now(timezone.utc)
    #print(current_date)

    # Loop through the list of users
    for user in users:
        # Get the user's name
        user_name = user['UserName']
        #print('hi')

        # Get the user's last login date
        last_login = user['PasswordLastUsed']
        #print(last_login)

        # Calculate the number of days since the user last logged in
        days_since_login = (current_date - last_login).days
        
        # Check if the user has not logged in for 2 months (60 days)
        if days_since_login > 60:
            # Send a warning email to the user
            subject = "Your console access is about to be removed"
            message = "You have not logged in to the console for 2 months. Your console access will be removed in 1 month. Please log in to the console as soon as possible to keep your access."
            sns.publish(TopicArn="arn:aws:sns:us-east-1:123456789012:MyTopic", Message=json.dumps({'default': message}), Subject=subject)
            
        elif days_since_login > 90:
            # Send a reminder email to the user
            subject = "Reminder: Your console access is about to be removed"
            message = "You have not logged in to the console for 3 months. Your console access will be removed soon. Please log in to the console as soon as possible to keep your access."
            sns.publish(TopicArn="arn:aws:sns:us-east-1:123456789012:MyTopic", Message=json.dumps({'default': message}), Subject=subject)


lambda_handler({}, {})