import sqlite3


def insert_query(query):
    connection, cursor = get_connection()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return True


def select_query():
    pass


def update_query():
    pass


def get_connection():
    connection = sqlite3.connect("database.sqlite3")
    cursor = connection.cursor()
    return (connection, cursor)


def init_db():
    create_ipv4_table = "CREATE TABLE ipv4_nodes (ip TEXT NOT NULL PRIMARY KEY, locked NULL)"
    create_ipv6_table = "CREATE TABLE ipv6_nodes (ip TEXT NOT NULL PRIMARY KEY, locked NULL)"
    insert_query(create_ipv4_table)
    insert_query(create_ipv6_table)


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
        return node
    else:
        return False


def get_unlocked_nodes(table):
    connection, cursor = get_connection()
    cursor.execute("SELECT ip FROM {} WHERE locked = 'UNLOCKED'".format(table))
    unlocked_nodes = cursor.fetchall()
    connection.close()
    unlocked_nodes_list = []
    for node in unlocked_nodes:
        unlocked_nodes_list.append(node[0])
    if unlocked_nodes_list:
        return unlocked_nodes_list
    else:
        return False