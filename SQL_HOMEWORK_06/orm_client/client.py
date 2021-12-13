import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from model.model import Base


class MysqlOpmClient:

    def __init__(self, user, password, db_name, host='127.0.0.1', port='3306'):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port

        self.engine = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def execute_query(self, query, fetch=True):
        result = self.connection.execute(query)
        if fetch:
            result.fetchall()

    def recreate_db(self):
        self.connect(db_created=False)

        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()

    def create_string_counter(self):
        if not inspect(self.engine).has_table('call_count'):
            Base.metadata.tables['call_count'].create(self.engine)

    def create_type_counter(self):
        if not inspect(self.engine).has_table('types_count'):
            Base.metadata.tables['types_count'].create(self.engine)

    def create_url_counter(self):
        if not inspect(self.engine).has_table('most_callable_urls'):
            Base.metadata.tables['most_callable_urls'].create(self.engine)

    def create_five400(self):
        if not inspect(self.engine).has_table('five_big400'):
            Base.metadata.tables['five_big400'].create(self.engine)

    def create_five500(self):
        if not inspect(self.engine).has_table('five_big500'):
            Base.metadata.tables['five_big500'].create(self.engine)
