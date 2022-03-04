from datetime import datetime
from alien_vault import verify_ipv4_node
from telegram_config import *
import requests
import os



def get_time():
    current_time = datetime.now()
    current_time = current_time.strftime("%d-%m-%Y_%H:%M")
    return  current_time


def txt_alerter(table, node):
    current_time = get_time()
    f = open('logs/alerts/{}_alert.txt'.format(table), 'a')
    f.write(node + "\n")
    f.close()

    f = open('logs/alerts/{}_alert_log.txt'.format(table), 'a')
    f.write(current_time + " " + node + " has been appended\n")
    f.close()


def log_updating(table, node):
    current_time = get_time()
    f = open('logs/alerts/{}_update_log.txt'.format(table), 'a')
    f.write(current_time + " " + node + " has been locked\n")
    f.close()


def simple_telegram_alert(node):
    current_time = get_time()
    message = "{}\nДобавлен адрес {}\n".format(current_time, node)
    alien_vault_results = verify_ipv4_node(node)
    if alien_vault_results:
        message += "Страна: {}\n".format(alien_vault_results["country_name"])
        if alien_vault_results["tags"]:
            message += "Тэги AlienVault:\n"
            for tag in alien_vault_results["tags"]:
                message += (tag + "\n")

    for chat in CHATS:
        r = requests.get(API_URL+"sendMessage?chat_id={}&text={}".format(str(chat), message))

"""
def send_file_with_unlocked_nodes(filename, chat):
    #Костыль
    cmd = "curl  -F \"chat_id={}\" -F document=@{} {}sendDocument"
    os.system(cmd.format(chat, filename, api_url))
"""

def log_unlocked_nodes(table, unlocked_nodes):
    current_time = get_time()
    f = open("logs/unlocked_nodes/{}_{}_unlocked.txt".format(current_time, table), "a")
    for node in unlocked_nodes:
        f.write(node+"\n")
    f.close()
    return "logs/unlocked_nodes/{}_{}_unlocked.txt".format(current_time, table)
