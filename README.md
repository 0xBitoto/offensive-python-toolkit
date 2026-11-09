# Offensive Python Toolkit 🛡️

A collection of custom-built offensive security scripts, network tools, and exploit prototypes written in Python from scratch.

## Modules

### 01. Networking Basics
* **`hello_socket.py`**: Raw TCP socket implementation connecting to remote web servers on port 80. Crafts raw HTTP/1.1 requests, executes a live TCP 3-way handshake without external libraries, and extracts server response headers (banner grabbing).

## Target Roadblock & Milestones
* [x] Low-level TCP Socket Connection & Banner Grabbing
* [ ] Multi-threaded TCP Port Scanner
* [ ] Directory & Endpoint Brute-Forcer
* [ ] Scapy Packet Sniffer & ARP Poisoner
