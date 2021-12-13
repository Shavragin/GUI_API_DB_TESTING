from sqlalchemy import String, Integer, Column

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CallCount(Base):
    __tablename__ = 'call_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<CallCount" \
               f"id={self.id}" \
               f"quantity = {self.strings}>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    strings = Column(Integer, nullable=False)


class TypeCount(Base):
    __tablename__ = 'types_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"TypeCount" \
               f"id={self.id}" \
               f"get= {self.get_strings}" \
               f"post= {self.post_strings}" \
               f"put= {self.put_strings}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    get_strings = Column(Integer, nullable=False)
    post_strings = Column(Integer, nullable=False)
    put_strings = Column(Integer, nullable=False)


class MostCallableURL(Base):
    __tablename__ = 'most_callable_urls'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"MostCallableURL" \
               f"id={self.id}" \
               f"url= {self.url}" \
               f"url_quantity= {self.url_quantity}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(1000), nullable=False)
    url_quantity = Column(Integer, nullable=False)


class FiveBig400(Base):
    __tablename__ = 'five_big400'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"FiveBig400" \
               f"id={self.id}" \
               f"get= {self.get_strings}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(1000), nullable=False)
    status_code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(100), nullable=False)


class FiveBig500(Base):
    __tablename__ = 'five_big500'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"FiveBig500" \
               f"id={self.id}" \
               f"ip={self.ip}" \
               f"quantity={self.quantity}"

    id = Column(Integer, primary_key=True, nullable=False)
    ip = Column(String(30), nullable=False)
    quantity = Column(Integer, nullable=False)
