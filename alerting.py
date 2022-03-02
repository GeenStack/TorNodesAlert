from datetime import datetime
from alien_vault import verify_ipv4_node
import requests
import os

token = ""
api_url = "https://api.telegram.org/bot{}/".format(token)


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


def simple_telegram_alert(node, chat):
    current_time = get_time()
    message = "{} Добавлен адрес {}\n".format(current_time, node)
    alien_vault_tags = verify_ipv4_node(node)
    if alien_vault_tags:
        message += "Тэги AlienVault:\n"
        for tag in alien_vault_tags:
            message += (tag + "\n")

    r = requests.get(api_url+"sendMessage?chat_id={}&text={}".format(str(chat), message))


def send_file_with_unlocked_nodes(filename, chat):
    #Костыль
    cmd = "curl  -F \"chat_id={}\" -F document=@{} {}sendDocument"
    os.system(cmd.format(chat, filename, api_url))


def log_unlocked_nodes(table, unlocked_nodes):
    current_time = get_time()
    f = open("logs/unlocked_nodes/{}_{}_unlocked.txt".format(current_time, table), "a")
    for node in unlocked_nodes:
        f.write(node+"\n")
    f.close()
    return "logs/unlocked_nodes/{}_{}_unlocked.txt".format(current_time, table)
