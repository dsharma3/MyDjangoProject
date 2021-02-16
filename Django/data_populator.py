import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoApp.settings')
import django
django.setup()

import random
from pollapp.models import Webpage,Topic
from faker import Faker


fakegen=Faker()
topics = ['Search','Social', 'Marketplace','News','Games']
def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic = top, url=fake_url, name = fake_name)[0]
        webpg.save()
if __name__ == '__main__':
    print("populating scripts")
    populate(20)
    print('population complete')
    