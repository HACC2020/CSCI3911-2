import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Guest(models.Model):
    guest_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.guest_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Meeting(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    meeting_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.meeting_text
