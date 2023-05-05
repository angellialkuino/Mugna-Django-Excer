import requests
from django.core.management.base import BaseCommand
from exercises.models import Book, Author


class Command(BaseCommand):
    help = "Add books and authors from gutendex"

    # def add_arquement(self, parser):

    def handle(self, *args, **options):
        url = "http://gutendex.com/books/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for result in data["results"]:
                author_name = result["authors"][0]["name"]
                last_name, first_name = author_name.split(", ")
                author, _ = Author.objects.get_or_create(
                    last_name=last_name, first_name=first_name
                )

                book, _ = Book.objects.get_or_create(
                    title=result.get("title"), author=author
                )
        else:
            self.stdout.write(self.style.ERROR("Failed to import books and authors"))
