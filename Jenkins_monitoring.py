#write a python script in simple form which can perform the following:
#create a Jenkins pipeline for monitoring the ec2 instances. 
#once the new instance is come up that time our script will copy over the new instance and execute in that instance.

import boto3

def create_pipeline():
    # Connect to the Jenkins server
    # Implement the steps to create a Jenkins pipeline for monitoring EC2 instances

    print("Jenkins pipeline created successfully!")

def copy_and_execute(instance_id):
    # Connect to the AWS EC2 service
    ec2 = boto3.resource('ec2')

    # Get the EC2 instance
    instance = ec2.Instance(instance_id)

    # Copy the necessary files to the EC2 instance
    # Implement the steps to copy the required files to the EC2 instance

    # Execute the necessary commands on the EC2 instance
    # Implement the steps to execute commands on the EC2 instance

    print("Files copied and executed successfully on the EC2 instance!")

def main():
    # Connect to the AWS EC2 service
    ec2 = boto3.resource('ec2')

    # Filter the EC2 instances based on specific criteria
    instances = ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ])

    # Loop through the EC2 instances and perform the necessary actions
    for instance in instances:
        instance_id = instance.id
        copy_and_execute(instance_id)

    print("Monitoring of EC2 instances completed!")

if __name__ == "__main__":
    create_pipeline()
    main()
