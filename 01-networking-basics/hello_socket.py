import socket

# 1. Create a raw TCP/IPv4 socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Perform the TCP 3-way handshake with google.com on port 80
client.connect(("142.251.37.78", 80))

# 3. Construct a raw HTTP GET request ( must end with two new lines \r\n\r\n)
request = "GET / HTTP/1.1\r\nHost: google.com\r\nConnection: close\r\n\r\n"

# 4. Sockets only send bytes, so we .encode() the string to bytes
client.sendall(request.encode())

# 5. Receive up to 4096 bytes of the server's reply
response = client.recv(4096)

# 6. Decode bytes back to readable text and print the server's banner/header
print(response.decode())

# 7. Close the connection
client.close()


