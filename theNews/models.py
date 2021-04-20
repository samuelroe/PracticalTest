from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

class newsStory(models.Model):
    storyHeading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    storyContent = models.CharField(max_length=200)

    def __str__(self):
        return self.storyHeading
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.storyContent