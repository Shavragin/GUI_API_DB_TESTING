import socket
import json
from settings import MOCK_PORT, MOCK_HOST
# import settings
# url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'
url = f'http://{MOCK_PORT}:{MOCK_HOST}'

class SocketClient:

    def client_connecttion(self, host, port):
        # создаём объект клиентского сокета
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # выставляем ожидание для сокета
        client.settimeout(0.1)
        # устанавливаем соединение
        client.connect((host, port))
        return client

    def listener(self, client):
        total_data = []
        try:
            while True:
                data = client.recv(4096)
                if data:
                    print(f'received data: {data}')
                    total_data.append(data.decode())
                else:
                    break
        except socket.timeout as e:
            print(e)
        finally:
            client.close()
            return ''.join(total_data).splitlines()


    def socket_client_get(self, user):

        params = f'/get_login_status/{user}'
        client = self.client_connecttion(MOCK_HOST, int(MOCK_PORT))
        # создаем и выполняем запрос
        request = f'GET {params} HTTP/1.1\r\nHost:{MOCK_HOST}\r\n\r\n'
        client.send(request.encode())

        data = self.listener(client)
        return data
        # print(data)
        # assert json.loads(data[-1])['age'] > 0


    def socket_client_post(self, user):
        params = '/post_new_user_status'

        client = self.client_connecttion(MOCK_HOST, int(MOCK_PORT))
        data = {
            "name": user
        }
        request = f'POST {params} HTTP/1.1\r\nHost:{MOCK_HOST}\r\nContent-Type: application/json\r\nContent-Length: 100\r\n\r\n{data}'
        # request = 'POST /post_new_user_status HTTP/1.1\r\nHost:127.0.0.1\r\nContent-Type: application/json\r\nContent-Length: 100\r\n\r\n{"name": "Anton}'
        client.send(request.encode())
        data = self.listener(client)
        return data

    def socket_client_put(self, user, status):
        params = '/change_status_user'
        client = self.client_connecttion(MOCK_HOST, int(MOCK_PORT))
        data = {
            "name": user,
            "status": status
        }
        request = f'PUT {params} HTTP/1.1\r\nHost:{MOCK_HOST}\r\nContent-Type: application/json\r\nContent-Length: 100\r\n\r\n{data}'
        client.send(request.encode())
        data = self.listener(client)
        return data

    def socket_client_delete(self, user):
        params = f'/delete_user/{user}'
        client = self.client_connecttion(MOCK_HOST, int(MOCK_PORT))
        request = f'DELETE {params} HTTP/1.1\r\nHost:{MOCK_HOST}\r\n\r\n'
        client.send(request.encode())
        data = self.listener(client)
        return data

