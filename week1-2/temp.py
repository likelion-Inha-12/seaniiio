from faker import Faker
fake = Faker('ko-KR')
fake.name()
fake.address()
print(fake.name())
print(fake.address())

test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)