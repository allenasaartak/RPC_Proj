"""
This is the client side code.
"""

import xmlrpc.client

server_ip = "127.0.0.1"
server = xmlrpc.client.ServerProxy(f'http://{server_ip}:8000')
print(f"Connected to RPC server at {server_ip}:8000")

while True:
  
    command = input("Enter command to execute on remote PC (type 'exit' to quit): \n--> ")
    if command.lower() == 'exit':
        print("The RPC is now exiting..")
        break

    try:
        response = server.execute_command(command)
        print("Command output:")
        print(response)
    except Exception as e:
        print(f"Error: {e}")
