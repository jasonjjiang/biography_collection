from django.contrib import admin
# import your models here
from .models import Biography, Status

# Register your models here
admin.site.register(Biography)
admin.site.register(Status)