# anisble-CM
This repository has Anisble scripts, etc needed to configure a MongoDB Cloud Manager demo in AWS EC2


# Assumptions
You have already installed and properly configured:
* Ansible
* the AWS CLI

#Usage
## Configuration
1. Modify the ansible.cfg file to make sure it is using the correct PEM file for your target instances

#Setting up a demo
1. Create your EC2 instances - you will need either the public IP addresses or Public DNS entries later, so keep the EC page up.
2. Log into Cloud Manager and choose your organization - creating one if needed.
3. Create a new Cloud Manager Deployment
3. Click the "Build New" button on Deployment page (below)
![alt text](https://github.com/jsstokes/ansible/blob/master/Screen-1.png "Logo Title Text 1")

 
