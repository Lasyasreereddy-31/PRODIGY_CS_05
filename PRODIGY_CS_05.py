import socket

def packet_sniffer():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind(("127.0.0.1", 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print("Packet sniffer started... Press Ctrl+C to stop")

    try:
        while True:
            packet = s.recvfrom(65565)
            print("Packet captured:", packet[0][:20])
    except KeyboardInterrupt:
        print("\nSniffer stopped")

packet_sniffer()

