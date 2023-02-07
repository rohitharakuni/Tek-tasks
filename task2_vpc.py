#Write a python script which can perform the following: We need alerts to notify us when A VPC is getting full

import boto3
import re

# Connect to the EC2 service
ec2 = boto3.client('ec2')

# Define the threshold for sending the alert (in GB)
THRESHOLD = 80

# Get information about all the VPCs
vpcs = ec2.describe_vpcs()

# Iterate through each VPC
for vpc in vpcs['Vpcs']:
    # Get the VPC ID
    vpc_id = vpc['VpcId']

    # Get the usage statistics for the VPC
    usage = ec2.describe_vpc_attribute(VpcId=vpc_id, Attribute='enableDnsSupport')

    # Extract the usage value as a float
    usage_value = float(re.search("[0-9.]+", usage['VpcId']).group(0))

    # Check if the usage is above the threshold
    print(usage_value)
    if usage_value > THRESHOLD:
        # Send an alert
        print(f"VPC {vpc_id} is above the threshold at {usage_value} GB")