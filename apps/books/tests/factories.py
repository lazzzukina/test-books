import factory
from faker import Faker

from apps.books.models import Book

fake = Faker()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    isbn = factory.LazyAttribute(lambda x: fake.unique.numerify(text='##########123'))

    title = factory.Faker('sentence')
    author = factory.Faker('name')
    published_date = factory.Faker('date')
    pages = factory.Faker('random_int', min=50, max=1000)
    cover = factory.Faker('image_url')
    language = factory.Faker('language_name')
