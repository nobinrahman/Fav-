import ipaddress

def generate_ip_list(start_subnet, end_subnet):
    start_ip = ipaddress.IPv4Address(start_subnet.split('/')[0])
    end_ip = ipaddress.IPv4Address(end_subnet.split('/')[0])

    ip_list = []
    for ip_int in range(int(start_ip), int(end_ip) + 1):
        ip_addr = ipaddress.IPv4Address(ip_int)
        ip_list.append(str(ip_addr))

    return ip_list

# Example usage
start_subnet = '192.168.0.0/24'
end_subnet = '192.168.1.0/24'
ip_list = generate_ip_list(start_subnet, end_subnet)

print(ip_list)
