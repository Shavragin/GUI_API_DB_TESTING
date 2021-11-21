from model.model import CallCount, TypeCount, MostCallableURL, FiveBig400
from utils.parser import get_calls_quantity, obtain_type_quantity

class MysqlORMBuilder:

    def __init__(self, client):
        self.client = client
        self.quantity = get_calls_quantity()
        self.type_count = obtain_type_quantity()

    def create_quantity(self):
        quantity = CallCount(strings=self.quantity)

        self.client.session.add(quantity)
        self.client.session.commit()
        return quantity

    def create_type_quantity(self):
        get = self.type_count[0]
        post = self.type_count[1]
        put = self.type_count[2]

        type_count = TypeCount(
            get_strings=get,
            post_strings=post,
            put_strings=put
        )

        self.client.session.add(type_count)
        self.client.session.commit()
        return type_count

    def create_url_quantity(self, url, quantity):
        type_count = MostCallableURL(
            url=url,
            url_quantity=quantity
        )

        self.client.session.add(type_count)
        self.client.session.commit()
        return type_count

    def create_400_quantity(self, url, status_code, size, ip):
        five_big400 = FiveBig400(
            url=url,
            status_code=status_code,
            size=size,
            ip=ip
        )

        self.client.session.add(five_big400)
        self.client.session.commit()
        return five_big400




