import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe
# Create your models here.


class Guest(models.Model):
    name = models.CharField(max_length=30)
    badge_id = models.CharField(max_length=30, blank=True)
    checked_in = models.BooleanField()

    def getName(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s | Checked In: %s' % (self.name, str(self.checked_in))
# Create your models here.

# Meeting_title = Meeting_room


class Meeting(models.Model):
    guest = models.OneToOneField(Guest, on_delete=models.CASCADE)
    meeting_room = models.CharField(max_length=30)
    meeting_desc = models.CharField(max_length=200)
    time_slot = models.DateTimeField()

    def getMeetingRoom(self):
        return self.meeting_room

    def getMeetingDesc(self):
        return self.meeting_desc

    def getMeetingInfo(self):
        return '%s %s' % (self.meeting_room, self.meeting_desc)

    def getFormattedTime(self):
        return self.time_slot.strftime("%c")

    def guest_link(self):
        return mark_safe('<a href="%s">%s</a>' % (reverse("admin:pages_guest_change", args=(self.guest.pk,)), escape(self.guest.getName())))

    guest_link.short_description = 'guest'

    # def guest_link(self):
    #     return '<a href="%s">%s</a>' % (reverse("admin:pages_guest_change", args=(self.guest.id,)), escape(self.guest))

    def __str__(self):
        return '%s at %s' % (self.meeting_room, self.time_slot.strftime("%c"))

    guest.allow_tags = True
