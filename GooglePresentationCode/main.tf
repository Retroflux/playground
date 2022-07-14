terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

#internet gateway
resource "aws_internet_gateway" "app_gateway" {
  vpc_id = aws_vpc.client-server-VPC.id
}

#VPC
resource "aws_vpc" "client-server-VPC" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "2022-07-18_GoogleCodeExample",
    Resource_Type = "VPC"
  }
}

#subnet1
resource "aws_subnet" "subnet1" {
  vpc_id     = aws_vpc.client-server-VPC.id #grabs VPC above
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-west-2a"

  tags = {
    Name = "2022-07-18_GoogleCodeExample",
    Resource_Type = "Subnet"
  }
}


#non-default route table
resource "aws_route_table" "route-table" {
  vpc_id = aws_vpc.client-server-VPC.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.app_gateway.id
  }

  tags = {
    Name = "2022-07-18_GoogleCodeExample"
  }
}

#route table association
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet1.id
  route_table_id = aws_route_table.route-table.id
}

#security groups
resource "aws_security_group" "open-port-12052" {
  name        = "port-12052"
  description = "Allow Inbound-Only Traffic to 12052"
  vpc_id      = aws_vpc.client-server-VPC.id

    ingress {
    description      = "HTTPS"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
#    cidr_blocks      = [aws_vpc.client-server-VPC] #TODO switch to VPC once it's working
    cidr_blocks      = ["0.0.0.0/0"] #TODO switch to VPC once it's working
  }

  ingress {
    description      = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
#    cidr_blocks      = [aws_vpc.client-server-VPC] #TODO switch to VPC once it's working
    cidr_blocks      = ["0.0.0.0/0"] #TODO switch to VPC once it's working
  }

  ingress {
    description      = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
#    cidr_blocks      = [aws_vpc.client-server-VPC] #TODO switch to VPC once it's working
    cidr_blocks      = ["0.0.0.0/0"] #TODO switch to VPC once it's working
  }
    ingress {
    description      = "SocketProtocol"
    from_port        = 12052
    to_port          = 12052
    protocol         = "tcp"
#    cidr_blocks      = [aws_vpc.client-server-VPC.cidr_block] #TODO switch to VPC once it's working
    cidr_blocks      = ["0.0.0.0/0"] #TODO switch to VPC once it's working
  }
  # TODO lock down after initial testing
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_12052"
  }
}

resource "aws_network_interface" "webserver_nic" {
  subnet_id = aws_subnet.subnet1.id
  private_ips = ["10.0.1.50"]
  security_groups = [aws_security_group.open-port-12052.id]
}

resource "aws_network_interface" "webclient1_nic" {
  subnet_id = aws_subnet.subnet1.id
  private_ips = ["10.0.1.51"]
  security_groups = [aws_security_group.open-port-12052.id]
}

resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.webserver_nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [aws_internet_gateway.app_gateway]
}

resource "aws_eip" "client1" {
  vpc                       = true
  network_interface         = aws_network_interface.webclient1_nic.id
  associate_with_private_ip = "10.0.1.51"
  depends_on = [aws_internet_gateway.app_gateway]
}
#
#data "template_file" "server-init" {
#  template = "${file("{path.module}/init.tpl")}"
#}

resource "aws_instance" "app_server" {
  ami               = "ami-0d70546e43a941d70" #Ubuntu 22
  instance_type     = "t2.micro"
  availability_zone = "us-west-2a"
  key_name          = "main-key"
  network_interface {
    device_index         = 0
    network_interface_id = aws_network_interface.webserver_nic.id
  }

  tags = {
    Host          = "Server"
    Name          = "2022-07-18_GoogleCodeExample"
    AMI           = "Ubuntu22"
    Resource_Type = "EC2"
  }
  user_data = file("init-server.sh")
}

resource "aws_instance" "app_client1" {
  ami               = "ami-0d70546e43a941d70" # Ubuntu 22
  instance_type     = "t2.micro"
  availability_zone = "us-west-2a"
  key_name          = "client1-key"

  network_interface {
    device_index         = 0
    network_interface_id = aws_network_interface.webclient1_nic.id
  }
  tags = {
    Host          = "Client-1"
    Name          = "2022-07-18_GoogleCodeExample"
    AMI           = "Ubuntu22"
    Resource_Type = "EC2"
  }
  user_data = file("init-client.sh")
  #  <<EOF
  #                #!/bin/bash
  #                sudo apt update
  #                sudo apt upgrade -y
  #                sudo apt install git -y
  #                sudo apt install gcc -y
  #                sudo apt install make -y
  #                git clone https://github.com/Retroflux/playground/tree/main/GooglePresentationCode
  #                EOF
  #}
}
#               git clone https://github.com/Retroflux/playground/tree/main/GooglePresentationCode
#               make > output.txt
#               ./server 12052
