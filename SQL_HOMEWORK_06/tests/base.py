import pytest

from model.model import CallCount, TypeCount, MostCallableURL, FiveBig400, FiveBig500
from orm_client.client import MysqlOpmClient
from utils.builder import MysqlORMBuilder


class BuilderBase:

    @pytest.fixture(autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOpmClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)

    def get_counter(self):
        self.mysql.session.commit()
        counter = self.mysql.session.query(CallCount)
        return counter.all()

    def obtain_type(self):
        self.mysql.session.commit()
        get_count = self.mysql.session.query(TypeCount)
        return get_count.all()

    def get_url_quantity(self):
        self.mysql.session.commit()
        calls = self.mysql.session.query(MostCallableURL)
        return calls.all()

    def get_size_quantity(self):
        self.mysql.session.commit()
        sizes = self.mysql.session.query(FiveBig400)
        return sizes.all()

    def get_500_quantity(self):
        self.mysql.session.commit()
        sizes = self.mysql.session.query(FiveBig500)
        return sizes.all()
