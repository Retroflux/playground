*E2.1*

Generated keypairs within the EC2 dashboard (devassoc); RSA/.ppk format; added a tag, so I know to 
delete it later.

Note: Make sure you're downloading the correct file type! If you're using PuTTy, then choose the .ppk; otherwise you
are likely going to want to use the openSSH style of key.

*E2.2*

Reminder that you can search for services. In this case, I moved from the keypair generation in 2.1 directly to 
the VPC dashboard with the search - very useful shortcut. Launching the VPC wizard from there.

NAT instances were removed from the wizard at some point after this book's publishing.
https://stackoverflow.com/questions/65862880/unable-to-select-use-a-nat-instance-instead-in-aws-vpc-wizard

In order to continue, you first have to create a NAT instance from within the VPC console. You can then fill in the
values suggested in E2.2 to continue. Steps for generating the NAT instance below:

1. Allocate an elastic IP from the sidebar, under the submenu Elastic IP.
2. After this, you can use the elastic IP to set up the NAT instance from within the VPC wizard.
   1. NOTE: do not create a NAT gateway directly - you just want the elastic IP, and then the wizard will build it.
3. Copy the VPC ID generated to a text document. It should be similar to: vpc-099az9bcf5af9e677

*E2.3*

This seems similar to the exercises in Ch1, though now the IAM role is going to be associated with a cloud item. The
only new learning point is the tags, but this has been covered in previous Ch2 notes.

*E2.4*

A lot of this interface has changed, but you don't need to enter the advanced except to paste the following:

#!/bin/bash
yum install httpd -y
systemctl start httpd
systemctl enable httpd

- After that, choose the correct instance type, set up the security group rules (in the tutorial, these are just Add Rule)
and then launch (the review panel is on the right)
- Also note that you set up the key pair from within this setup, so step 16 should happen before step 14!
- Takes a bit of time to spin up the instance, so step 19 will take a moment

*E2.5*

Note that 

Output from the suggested commands in the tutorial


_Shows the available metadata fields_
curl 169.254.169.254/latest/meta-data/
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
managed-ssh-keys/
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/

curl 169.254.169.254/latest/meta-data/instance-id

$ curl 169.254.169.254/latest/meta-data/instance-id
[REDACTED]

aws translate translate-text --text "Hello World." --source-language-code en --target-language-code fr --region us-west-2

{
    "TargetLanguageCode": "fr",
    "TranslatedText": "Bonjour tout le monde.",
    "SourceLanguageCode": "en"
}

*E2.8*

Created the private server in 2.6/2.7, which included startup code to create a polly file. copied it from the private
instance to the public instance and placed the file in /var/www/html/instance.mp3. Accessed that via a web browser
(http://server-ip/instance.mp3), and downloaded it. File stored and uploaded to git.