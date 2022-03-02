from db_module import *
from alerting import *


def lock_node(table, node):
    connection, cursor = get_connection()
    check_node(table, node)
    query = "UPDATE {} set locked='LOCKED' WHERE ip='{}'".format(table, node)
    cursor.execute(query)
    connection.commit()
    connection.close()
    log_updating(table, node)
    return True

def lock_nodes_list(table, list_to_block):
    for node in list_to_block:
        lock_node(table, node)
    return True