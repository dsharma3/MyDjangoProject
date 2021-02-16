from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=264)
    url = models.URLField()

    def __str__(self):
        return self.name

