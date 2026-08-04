import socket #ağ programlama yapıcaksan akla ilk socket modülü gelir internet üzerindeki veri iletişmin temelidir
address =  socket.gethostbyname(socket.gethostname())
port = 5000
byte = 1024
server =socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)#udp de tek socket yeterlidir bağlantı kurulmadığı için 

server.bind((address, port))#gelen paketleri işletim sistemine söylüyor bu ip ve porttan gelcek udp paketlerini dinlicem demek 
#bind fonksiyonuna tek bir argüman gönderiyorum. Bu argümanın içinde iki bilgi var: IP ve port.
#server.bind(address, port) şu anlama gelir: bind fonksiyonuna 2 ayrı argüman gönderiyorum. Ama bind() bunu kabul etmez.
 #socketler ağ üzerinden string gönderemez her aslında byte dizisidir
#karşı taraftan gelen mesajı almak için bu fonku kullandım benim ona cevap vermem için bana gönderdiği mesaj ve gönderenin adresi lazım
#message yi fonksiyonun döndürdüğü ilk değeri bi yere koymam gerektiği için kullandım
print("Server is working...")
while True:
    message ,address = server.recvfrom(byte)
    message=message.decode("utf-8")
    if message == "quit":
        break
    else:
        print(f"text: { message}")
        message = input("text: ")
        server.sendto(message.encode("utf-8"), address) #sendto ya göndermesini istediğimiz verileri veririz sendto bize veri vermez
server.close