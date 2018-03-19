#!/usr/bin/python
max_hosts = 3
hosts = []   
test = raw_input("Enter Public Name or IP Address (<ENTER> by itself after last entry): ")
while (test != ""):
    hosts.append(test)
    if len(hosts) == max_hosts:
        break
    test = raw_input("Enter Public Name or IP Address (<ENTER> by itself after last entry): ")

for host in hosts:
    print "Host Name: ", host

rsname = raw_input("Enter the result set name: ")
port = raw_input("Enter the port number for MongoDB: ")
mmsGroupId = raw_input("Please enter the mmsGroupId: ")
mmsApiKey = raw_input("Please enter the mmsApiKey: ")

connection_string = rsname+"/"
for host in hosts:
    connection_string += host+":27000,"
last_pos = connection_string.rfind(",")
print "Connection String: " + connection_string[0:last_pos]
host_file = open("hosts.test","w")
host_file.write("[local]\n")
host_file.write("127.0.0.1\n")
host_file.write("\n")
host_file.write("[demo]\n")
for host in hosts:
    host_file.write(host + "\n")

host_file.write("\n")
host_file.write("[demo:vars]\n")
host_file.write("conn_string=" + connection_string+"\n")
host_file.write("api_key="+ mmsApiKey+"\n")
host_file.write("mmsGroupId=" + mmsGroupId+"\n")



