import json
import socket

import requests

from settings import MOCK_PORT, MOCK_HOST

url = f'http://{MOCK_PORT}:{MOCK_HOST}'


class SocketClient:

    def client_connecttion(self, host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
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

    def client_get(self, user):
        params = f'/get_login_status/{user}'
        client = self.client_connecttion(MOCK_HOST, int(MOCK_PORT))

        request = f'GET {params} HTTP/1.1\r\nHost:{MOCK_HOST}\r\n\r\n'
        client.send(request.encode())

        data = self.listener(client)
        return data

    def client_delete(self, user):
        params = f'/delete_user/{user}'
        client = self.client_connecttion(MOCK_HOST, int(MOCK_PORT))
        request = f'DELETE {params} HTTP/1.1\r\nHost:{MOCK_HOST}\r\n\r\n'
        client.send(request.encode())
        data = self.listener(client)
        return data

    def client_post(self, name):
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'name': name})

        return requests.post('http://127.0.0.1:1234/post_new_user_status', headers=headers, data=data)

    def client_put(self, name, status):
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'name': name, 'status': status})
        return requests.put('http://127.0.0.1:1234/change_status_user', headers=headers, data=data)
