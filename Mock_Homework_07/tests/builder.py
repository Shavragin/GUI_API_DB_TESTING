from faker import Faker

faker = Faker()

def fake_name():
    return faker.first_name()


