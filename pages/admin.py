from django.contrib import admin
from .models import Meeting
from .models import Guest

# Register your models here.
# admin.site.register(Meeting)


class MeetingAdmin(admin.ModelAdmin):
    list_display = ("meeting_desc", "meeting_room", "time_slot")
    search_fields = ("meeting_room", "meeting_desc", )


class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "badge_id", "checked_in")
    search_fields = ("name", "badge_id")


admin.site.register(Meeting, MeetingAdmin)

admin.site.register(Guest, GuestAdmin)
