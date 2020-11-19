from django.contrib import admin
from .models import Meeting
from .models import Guest

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Guest)

admin.site.site_header = 'UH Security Staff Portal'
admin.site.site_title = 'UH Security Staff Portal |'
admin.site.index_title = ''
