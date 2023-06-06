#code from chatGPT

import socket
import struct
import time

def get_ntp_time(server='pool.ntp.org', port=123):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set timeout for the socket
    sock.settimeout(5)
    
    
    # NTP server address
    server_address = (server, port)
    
    # NTP request packet format (48 bytes total)
    # Leap indicator (2 bits), Version number (3 bits), Mode (3 bits)
    ntp_header = b'\x1b' + 47 * b'\0'
    
    try:
        # Send the NTP request packet
        sock.sendto(ntp_header, server_address)
        
        # Receive the response packet
        data, _ = sock.recvfrom(48)
        
        # Extract the transmit timestamp from the response packet
        transmit_time = struct.unpack('!12I', data)[10]
        
        # Convert the transmit timestamp to a UTC time
        ntp_time = transmit_time - 2208988800
        
        return ntp_time
    except socket.timeout:
        print("Connection timed out.")
    finally:
        # Close the socket
        sock.close()

if __name__ == '__main__':
    ntp_time = get_ntp_time()
    if ntp_time:
        print(f"NTP Time: {time.ctime(ntp_time)}")
