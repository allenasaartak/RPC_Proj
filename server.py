'''
This is the server's side code.
'''
from xmlrpc.server import SimpleXMLRPCServer
import subprocess
server = SimpleXMLRPCServer(('127.0.0.1', 8000))
print("RPC server is running on localhost at port 8000")
def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"
server.register_function(execute_command, 'execute_command')
server.serve_forever()
