import socket

host = "127.0.0.1"
port = 12345  

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Bağlantı noktası kullanılabilirliği için

sc.bind((host, port))

sc.listen(1)  # Dinleme sırasındaki maksimum bağlantı sayısı belirtilmelidir, burada 1

print(f"Listening on {host}:{port}...")

conn, addr = sc.accept()

if conn:
    print(f"{addr} kullanıcısı bağlandı.")

    while True:
        liData = conn.recv(1024)
        
        if not liData:  # Bağlantı kapandığında döngüden çık
            print("Bağlantı kapandı.")
            break

        message = liData.decode("utf-8")
        
        if message == "exit":
            print("Bağlantı kapatılıyor.")
            conn.close()
            break
        else:
            print(message)

        data = input("Message: ")

        if data == "exit":
            conn.sendall(data.encode("utf-8"))
            conn.close()
            print("Bağlantı kapatıldı.")
            break
        else:
            conn.sendall(data.encode("utf-8"))

sc.close()
