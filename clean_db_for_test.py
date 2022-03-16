import sqlite3
import db_module

def clean_data():
    connection, cursor = db_module.get_connection()
    cursor.execute("DELETE FROM ipv6_nodes WHERE ip='2001:067c:089c:0702:01ce:01ce:babe:0004'")
    connection.commit()
    cursor.execute("DELETE FROM ipv4_nodes WHERE ip='194.9.173.107'")
    connection.commit()
    connection.close()