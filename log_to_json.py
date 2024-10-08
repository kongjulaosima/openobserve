import datetime
import json
import os
import sys

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
logs_path = '/scholar-club/scholar-club-backend/logs'
try:
    date = str(sys.argv[1])
except:
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    #date = str(today)  #
    date = str(yesterday)


def traversal_folder(folder_path):
    logs_name_list = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            logs_name_list.append(file_name)
    return logs_name_list


logs_name_list = traversal_folder(parent_dir + logs_path)
json_list = []
print('date:', date)
for logs_name in logs_name_list:
    if logs_name[:10] == date:
        log_abs_path = parent_dir + logs_path + '/' + logs_name
        print('log_abs_path:', log_abs_path)
        with open(log_abs_path, 'r', encoding='utf8') as file:
            for line in file:
                list_info = line.split(' | ')
                d = {
                    'date': list_info[0][:10],
                    "time": list_info[0],
                    "module": list_info[1],
                    "funcName": list_info[2],
                    "line": list_info[3],
                    "levelname": list_info[4],
                    "message": list_info[5],
                }
                json_list.append(d)
try:
    nginx_path = '/home/lenovo/scholar-club/nginx/log/access.log'
    nginx_path2 = '/home/lenovo/scholar-club/nginx/log/error.log'
    with open(nginx_path, 'r', encoding='utf8') as file:
        for line in file:
            d = {
                'date': str(date),
                "type": 'access.log',
                "message": line,
            }
            json_list.append(d)
    with open(nginx_path2, 'r', encoding='utf8') as file:
        for line in file:
            d = {
                'date': str(date),
                "type": 'error.log',
                "message": line,
            }
            json_list.append(d)
except:
    pass
with open('logs.json', 'w', encoding='utf-8') as fw:
    json.dump(json_list, fw, indent=4, ensure_ascii=False)



with open('logs.txt', 'a', encoding='utf-8') as fw:
    fw.write('已经传输当前时间:{}'.format(datetime.datetime.now()) + '\n')



