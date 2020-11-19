from django.contrib import admin
from .models import Meeting
from .models import Guest

# Register your models here.
# admin.site.register(Meeting)


class MeetingAdmin(admin.ModelAdmin):
    list_display = ("meeting_room", "meeting_desc", "time_slot", "guest_link")
    search_fields = ("meeting_room", "meeting_desc",
                     "time_slot", "guest__name")


class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "badge_id", "checked_in")
    search_fields = ("name", "badge_id")
    def get_model_perms(self, request): return {}


admin.site.register(Meeting, MeetingAdmin)

admin.site.register(Guest, GuestAdmin)
