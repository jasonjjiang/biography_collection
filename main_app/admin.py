from django.contrib import admin
# import your models here
from .models import Biography, Status, Version

# Register your models here
admin.site.register(Biography)
admin.site.register(Status)
admin.site.register(Version)