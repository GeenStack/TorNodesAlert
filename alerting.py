from datetime import datetime
import requests
import os

token = ""
api_url = "https://api.telegram.org/bot{}/".format(token)


def get_time():
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    return "{} {} {} {}:{}:{}".format(year, month, day, hour, minute, second)


def get_undeline_time():
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    return "{}_{}_{}_{}_{}_{}".format(year, month, day, hour, minute, second)


def txt_alerter(table, node):
    current_time = get_time()
    f = open('{}_alert.txt'.format(table), 'a')
    f.write(node + "\n")
    f.close()

    f = open('{}_alert_log.txt'.format(table), 'a')
    f.write(current_time + " " + node + " has been appended\n")
    f.close()


def log_updating(table, node):
    current_time = get_time()
    f = open('{}_update_log.txt'.format(table), 'a')
    f.write(current_time + " " + node + " has been locked\n")
    f.close()


def simple_telegram_alert(node, chat):
    current_time = get_time()
    message = "{} Добавлена нода {}".format(current_time, node)
    r = requests.get(api_url+"sendMessage?chat_id={}&text={}".format(str(chat), message))


def send_file_with_unlocked_nodes(filename, chat):
    #Костыль
    cmd = "curl  -F \"chat_id={}\" -F document=@{} {}sendDocument"
    os.system(cmd.format(chat, filename, api_url))


def log_unlocked_nodes(table, unlocked_nodes):
    current_time = get_undeline_time()
    f = open("{}_unlocked.txt".format(current_time), "a")
    for node in unlocked_nodes:
        f.write(node+"\n")
    f.close()
    return "{}_unlocked.txt".format(current_time)
