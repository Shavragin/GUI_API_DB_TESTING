import pytest

from orm_client.client import MysqlOpmClient

def pytest_configure(config):
    orm_client = MysqlOpmClient(user='root', password='root', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        orm_client.recreate_db()
    orm_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        orm_client.create_string_counter()
        orm_client.create_type_counter()
        orm_client.create_url_counter()
        orm_client.create_five400()

    config.orm_client = orm_client

@pytest.fixture(scope="session")
def mysql_orm_client(request):
    client = request.config.orm_client
    yield client
    client.connection.close()
