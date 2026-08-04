import socket

address =  socket.gethostbyname(socket.gethostname())
port = 5000
byte = 1024
client =socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)#udp de tek socket yeterlidir bağlantı kurulmadığı için 

#udp clientta bind yapılmaz çünkü portu dinlemeye ihtiyacı yoktur sendto ile veri göndermeye ihtiyacı var

while True:
    message=input("text: ")

    client.sendto(message.encode("utf-8"), (address,port ))
    
    if message == "quit":
        break
    else:
       
        #sendto ya göndermesini istediğimiz verileri veririz sendto bize veri vermez
      
        message ,address = client.recvfrom(byte)
        message=message.decode("utf-8")
        print(f"text: { message}")
client.close()