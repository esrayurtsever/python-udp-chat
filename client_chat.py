import socket

address =  socket.gethostbyname(socket.gethostname())
port = 5000
byte = 1024
client =socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)

while True:
    message = input("text: ")

    client.sendto(message.encode("utf-8"), (address ,port ))
    
    if message == "quit":
        break
    else:
        message ,address = client.recvfrom(byte)
        message=message.decode("utf-8")
        print(f"text: { message}")
        
client.close()
