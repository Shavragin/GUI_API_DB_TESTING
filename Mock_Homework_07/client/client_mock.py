import socket
import json

# import settings
MOCK_HOST = '127.0.0.1'
MOCK_PORT = '8080'
# url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'
url = f'http://{MOCK_PORT}:{MOCK_HOST}'

class SocketClient:
    def test_with_socket_client(self):

        target_host = MOCK_PORT
        target_port = int(MOCK_HOST)

        params = '/get_user/123'

        # создаём объект клиентского сокета
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # выставляем ожидание для сокета
        client.settimeout(0.1)

        # устанавливаем соединение
        client.connect((target_host, target_port))

        # создаем и выполняем запрос
        request = f'GET {params} HTTP/1.1\r\nHost:{target_host}\r\n\r\n'
        client.send(request.encode())

        total_data = []

        while True:
        # читаем данные из сокета до тех пор пока они там есть
            data = client.recv(4096)
            if data:
                print(f'received data: {data}')
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        print(data)
        assert json.loads(data[-1])['age'] > 0