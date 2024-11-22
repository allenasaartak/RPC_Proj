# RPC_Proj
This project implements a Remote Procedure Call (RPC) system on a single computer using Python 3 and XML-RPC libraries. The server executes commands sent by the client via localhost, returning the results or errors. It’s ideal for learning RPC concepts and testing local inter-process communication.

Overview:
A simple Remote Procedure Call (RPC) system developed using Python 3.
Runs entirely on a single computer using the localhost interface (127.0.0.1).
Demonstrates bi-directional communication between a server and client process.

Key Features:

Server:
1. Listens for incoming commands on localhost and port 8000.
2. Executes shell commands using Python’s subprocess module.
3. Returns command output or error messages to the client.

Client:
1. Connects to the server using XML-RPC.
2. Sends terminal commands for execution.
3. Displays the results or error messages received from the server.

Technology Stack:
1.Programming Language: Python 3
2. Libraries:
  a. SimpleXMLRPCServer (for the server)
  b. xmlrpc.client (for the client)
  c. subprocess (for command execution)
  
Applications:
1. Educational purposes for learning RPC concepts.
2. Testing and debugging inter-process communication.
3. Demonstrating secure and local command execution.
   
Advantages:
1. Simple to set up and use on a single machine.
2. No network or firewall configurations required.
3. Efficient and lightweight communication.
