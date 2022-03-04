from get_nodes_list import *
from db_module import *
from alerting import *


def main():
    nodes_lists = get_nodes_lists()
    ipv4_nodes = nodes_lists["ipv4_nodes"]
#   ipv6_nodes = nodes_lists["ipv6_nodes"]

    for node in ipv4_nodes:
        if check_node("ipv4_nodes", node):
            txt_alerter("ipv4_nodes", node)
            simple_telegram_alert(node)
'''
    for node in ipv6_nodes:
        if check_node("ipv6_nodes", node):
            txt_alerter("ipv6_nodes", node)
            for chat in chats:
                simple_telegram_alert(node, chat)

    unlocked_ipv4_nodes = get_unlocked_nodes("ipv4_nodes")
    if unlocked_ipv4_nodes:
        log_filename = log_unlocked_nodes("ipv4_nodes", unlocked_ipv4_nodes)
        for chat in chats:
            #Alert file to telegram
            send_file_with_unlocked_nodes(log_filename, chat)
            pass

    unlocked_ipv6_nodes = get_unlocked_nodes("ipv6_nodes")
    if unlocked_ipv4_nodes:
        log_filename = log_unlocked_nodes("ipv6_nodes", unlocked_ipv6_nodes)
        for chat in chats:
            # Alert file to telegram
            send_file_with_unlocked_nodes(log_filename, chat)
            pass
'''

if __name__ == "__main__":
    main()