from django.contrib import admin
from .models import Meeting
from .models import Guest

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Guest)
