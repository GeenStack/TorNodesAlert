import requests


URL = "https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-exit-nodes.lst"


def get_nodes_lists():
    try:
        r = requests.get(URL)
        ip_list = r.text.split("\n")[:-1:]
        ipv4_nodes = []
        ipv6_nodes = []
        for ip in ip_list:
            if ip.find(":") != -1:
                ipv6_nodes.append(ip)
            else:
                ipv4_nodes.append(ip)

        return {"ipv4_nodes":ipv4_nodes, "ipv6_nodes":ipv6_nodes}

    except Exception as e:
        return False