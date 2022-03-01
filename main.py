from get_nodes_list import *
from db_module import *

def check_node(table, node):
    connecion, cursor = get_connection()
    query = "SELECT * FROM {} WHERE ip = '{}'".format(table, node)
    cursor.execute(query)
    data = cursor.fetchone()
    if not data:
        query = "INSERT INTO {} VALUES ('{}', '{}')".format(table, node, "UNLOCKED")
        cursor.execute(query)
        connecion.commit()
        connecion.close()
        print("append node {}".format(node))
        return node
    else:
        return False

def main():
    nodes_lists = get_nodes_lists()
    ipv4_nodes = nodes_lists["ipv4_nodes"]
    ipv6_nodes = nodes_lists["ipv6_nodes"]

    for node in ipv4_nodes:
        check_node("ipv4_nodes", node)
    for node in ipv6_nodes:
        check_node("ipv6_nodes", node)