import random
from faker import Faker
from django.utils import timezone
from apps.user.models import User
from apps.book.models import Book
from django.core.management.base import BaseCommand

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with few instances of Book and user model'

    def handle(self, *args, **options):

        for _ in range(20):
            user = User.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                is_active=True,
                is_staff=random.choice([True, False]),
                password=fake.password()
            )


            for _ in range(random.randint(4, 10)):
                book = Book.objects.create(
                    author=user,
                    title=fake.text(50),
                    isbn=fake.isbn13(),
                    publication_year=random.randint(1000, timezone.now().year),
                    brief_summary=fake.paragraph()
                )

            self.stdout.write(self.style.SUCCESS(f'Successfully created book "{book.title}"'))
