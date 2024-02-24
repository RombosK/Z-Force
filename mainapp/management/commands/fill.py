from django.core.management import BaseCommand

from mainapp.models import News


class Command(BaseCommand):

    def handle(self, *args, **options):
        news_list = []
        for i in range(1, 15):
            news_list.append(News(
                name=f"name#{i}",
                photo=f"photo#{i}",
                description="description"
            ))

        News.objects.bulk_create(news_list)

