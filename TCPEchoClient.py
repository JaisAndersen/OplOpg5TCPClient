from socket import *
import json

server_ip = '127.0.0.1'
server_port = 7
clientSocket = socket(AF_INET, SOCK_STREAM)

try:        
    clientSocket.connect((server_ip, server_port))
    while True:
           
        command = input("Enter command (Random, Add, Subtract): ").strip()
        parameters = input("Enter parameters (space-separated): ").strip().split()

        message = {
            "Command": command,
            "Parameters": parameters
        }

        json_message = json.dumps(message)

        clientSocket.sendall(json_message.encode('utf-8') + b'\n')

        response = clientSocket.recv(1024).decode('utf-8').strip()

        response_data = json.loads(response)
        if "Error" in response_data:
            print(f"Error: {response_data['Error']}")
        else:
            print(f"Result: {response_data['Result']}")

except Exception as e:
    print(f"Exception: {e}")

clientSocket.close()
print("Connection closed.")
