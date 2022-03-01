from datetime import datetime


def get_time():
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    return "{} {} {} {}:{}:{}".format(year, month, day, hour, minute, second)


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