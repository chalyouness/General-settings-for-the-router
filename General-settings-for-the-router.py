from netmiko import ConnectHandler
#Import the Netmiko library

# Define the router details
router = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',  # Replace with your router's IP address
    'username': 'your_username',
    'password': 'your_password',
    'secret': 'enable_secret',
}

# Connect to the router
net_connect = ConnectHandler(**router)
net_connect.enable()

# Define the configuration commands
config_commands = [
    'interface GigabitEthernet0/0',
    'ip address 192.168.2.1 255.255.255.0',
    'no shutdown',
    'exit',
    'router ospf 1',
    'network 192.168.2.0 0.0.0.255 area 0',
    'exit',
]

# Send configuration commands to the router
output = net_connect.send_config_set(config_commands)
print(output)

# Save the configuration
output = net_connect.save_config()
print(output)

# Disconnect from the router
net_connect.disconnect()
