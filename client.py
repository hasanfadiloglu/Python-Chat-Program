import socket

host = "127.0.0.1"
port = 12345  

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sc.connect((host, port))

while True:
    data = input("Message: ")
    
    if data == "exit":  # Doğrudan karşılaştırma
        sc.sendall(data.encode("utf-8"))
        print("Bir kullanıcı ayrıldı.")
        sc.close()
        break
    else:
        sc.sendall(data.encode("utf-8"))

    liData = sc.recv(1024)
    
    if not liData:  # Bağlantı kapandığında döngüden çık
        print("Sunucu bağlantıyı kapattı.")
        break

    message = liData.decode("utf-8")
    
    if message == "exit":
        print("Sunucu bağlantıyı kapattı.")
        sc.close()
        break
    else:
        print(message)
