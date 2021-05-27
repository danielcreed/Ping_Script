import os

Servers = \
    {"Server1": '192.168.16.10',
     "Server2": '192.168.16.11'
     }


ExternalHosts = \
    {"8.8.8.8": 'Google 1',
     "1.1.1.1": 'Google 2',
     "8.8.4.4": 'Google 3',
     "208.67.222.222": 'Cisco Dns',
     "52.138.20.176": 'Azure WebHosting'
     }

# Packing Server IP Lists into Dictionary Lists
ServerPack = Servers.items()
ExternalPack = ExternalHosts.items()


for key,value in ServerPack:

    response1 = os.popen(f"ping {value}").read()
    if "Received = 4" in response1:
        print(f"Internal UP {key} Ping Success")
    else:
        print(f"Internal Down {key} Ping Failure")


for key,value in ExternalPack:
    response = os.popen(f"ping {key}").read()
    if "Received = 4" in response:
        print(f"External UP {value} Ping Success")
    else:
        print(f"External Down {value} Ping Failure")