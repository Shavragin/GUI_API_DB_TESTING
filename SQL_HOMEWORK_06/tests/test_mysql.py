from tests.base import BuilderBase
from utils.parser import most_callable_url, most_5_4xx_url

class TestMySQL(BuilderBase):

    def prepare_urls(self):
        url_list = most_callable_url()
        for i in url_list:
            self.mysql_builder.create_url_quantity(i[0], i[1])

    def prepare_sizes(self):
        sizes = most_5_4xx_url()
        for i in sizes:
            self.mysql_builder.create_400_quantity(i, i[1][0], i[1][1], i[2])

    def test_strings_counter(self):
        self.mysql_builder.create_quantity()
        table = self.get_counter()
        assert len(table) == 1

    def test_get_counter(self):
        self.mysql_builder.create_type_quantity()
        types_table = self.obtain_type()
        assert len(types_table) == 1

    def test_url_quantity(self):
        self.prepare_urls()
        url_table = self.get_url_quantity()
        assert len(url_table) == 10

    def test_url_400_size_quantity(self):
        self.prepare_sizes()
        sizes_table = self.get_size_quantity()
        assert len(sizes_table) == 5
