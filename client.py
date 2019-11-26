from psutil import cpu_percent
import time
import socket
import requests


if __name__ == "__main__":
    default_server_port = '127.0.0.1:8001'
    print('введите ip_порт в формате 0.0.0.0:0000')
    server_ip_port = input()
    if server_ip_port == '':
        server_ip_port = default_server_port

    s = socket.socket()
    host = server_ip_port.split(':')[0]
    port = int(server_ip_port.split(':')[1])
    print('Задан адрес {} и порт {} сервера'.format(host, port))
    s.connect((host, port))
    address = 'http://' + server_ip_port + '/api/catcher/'

    count = 0
    while True:
        cpu_utilization = cpu_percent()                             # загрузка процессора в процентах
        print('Загрузка ЦП {}%'.format(cpu_utilization))
        url = address
        data = ({"message": {"name": cpu_utilization}})
        res = requests.post(url, json=data)
        print(res.text)
        time.sleep(10)                                              # ожидание 10 секунд
        count += 1
    s.close()
