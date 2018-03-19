# ansible-CM
This repository has Anisble scripts, etc needed to configure a MongoDB Cloud Manager demo in AWS EC2


# Assumptions
You have already installed and properly configured:
* Ansible
* the AWS CLI

# Usage
## Configuration
1. Modify the ansible.cfg file to make sure it is using the correct PEM file for your target instances

# Setting up a demo
1. Create your EC2 instances - you will need either the public IP addresses or Public DNS entries later, so keep the EC page up.
2. Log into Cloud Manager and choose your organization - creating one if needed.
3. Create a new Cloud Manager Deployment
3. Click the "Build New" button on Deployment page (below)
![alt text](https://github.com/jsstokes/ansible/blob/master/Screen-1.png "Build New Image")
4. One the following page ("Where would you like to deploy MongoDB?"), select "Deploy in other remote" button (below).
![alt text](https://github.com/jsstokes/ansible/blob/master/Screen-2.png "Deploy in other remote image")
5. Select "Create Replica Set" (below)
![alt text](https://github.com/jsstokes/ansible/blob/master/Screen-3.png "Create Replica Set")
5. Enter the values for Replica Set Name, Number of Nodes, and Data Directory Prefix.
  * __Make note of these values, you will need them later!!__
![alt text](https://github.com/jsstokes/ansible/blob/master/Screen-4.png "Replica Set Details")
6. Choose whether or not you want backups made of this Replica Set.
7. On the next page ("Install an Automation Agent on each server"), select the appropriate value from the "Install Agent List".
![alt text](https://github.com/jsstokes/ansible/blob/master/Screen-5.png "Install Agent image")
8. A popup will appear with instruction to configure the replica set member.  The anisble scripts will perform all of the configuration steps on each member.  Please make note of the mmsGroupId (see screen shot below), then click the "Agent API Keys" link.
![alt text](https://github.com/jsstokes/ansible/blob/master/Screen-6.png "Automation Agent Popup")

# Creating the Agent API Key
1. After following the instructions in the above section, you should be at the Agent API Page.




 
