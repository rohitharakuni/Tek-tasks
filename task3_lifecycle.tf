#Create a lifecycle manager policy for taking the backup of the ec2 instance volume every 12 hours once,
#and keep it only upcoming two volumes. rest of the volumes will delete automatically.
#These things needs to be automated via Terraform

provider "aws" {
  region = "us-west-2"
  access_key = ""
  secret_key = ""
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}

resource "aws_ebs_volume" "example" {
  availability_zone = "${aws_instance.example.availability_zone}"
  size              = "1"

  tags = {
    Name = "example-volume"
  }
}

resource "aws_volume_attachment" "example" {
  device_name = "/dev/sdf"
  volume_id   = "${aws_ebs_volume.example.id}"
  instance_id = "${aws_instance.example.id}"
}

module "ec2_lifecycle_manager_policy" {
  source = "terraform-aws-modules/ec2-lifecycle-manager/aws"

  policy_name        = "example-policy"
  volume_id          = "${aws_ebs_volume.example.id}"
  schedule_expression = "cron(0 */12 * * ? *)"
  retain_rule_count  = 2

  tags = {
    Environment = "prod"
  }
}

#In this example, a new EC2 instance and EBS volume are created, and the volume is attached to the instance. 
#Then, a lifecycle manager policy is created for the volume. 
#The policy takes a backup of the volume every 12 hours and retains only the 2 latest backups, with all older backups being deleted automatically.