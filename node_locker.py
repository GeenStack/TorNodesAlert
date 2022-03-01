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