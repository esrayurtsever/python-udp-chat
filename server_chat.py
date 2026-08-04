import socket 
address =  socket.gethostbyname(socket.gethostname())
port = 5000
byte = 1024
server = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)#udp de tek socket yeterlidir bağlantı kurulmadığı için 

server.bind((address, port))

print("Server is working...")

while True:
    message , address = server.recvfrom(byte)
    message=message.decode("utf-8")
    if message == "quit":
        break
    else:
        print(f"text: { message}")
        message = input("text: ")
        server.sendto(message.encode("utf-8"), address) #sendto ya göndermesini istediğimiz verileri veririz sendto bize veri vermez

server.close()
