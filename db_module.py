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