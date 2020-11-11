import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Guest(models.Model):
    name = models.CharField(max_length=30)
    badge_id = models.CharField(max_length=30)
    checked_in = models.BooleanField()

    def __str__(self):
        return '%s     |     BadgeID: %s     |      Checked In: %s' % (self.name, self.badge_id, str(self.checked_in))
# Create your models here.


class Meeting(models.Model):
    guest = models.ManyToManyField(Guest)
    meeting_title = models.CharField(max_length=30)
    meeting_desc = models.CharField(max_length=200)
    time_slot = models.DateTimeField()

    def getMeetingTitle(self):
        return self.meeting_title

    def getMeetingDesc(self):
        return self.meeting_desc

    def getMeetingInfo(self):
        return '%s %s' % (self.meeting_title, self.meeting_desc)

    def __str__(self):
        return '%s at %s' % (self.meeting_title, self.time_slot.strftime("%c"))
