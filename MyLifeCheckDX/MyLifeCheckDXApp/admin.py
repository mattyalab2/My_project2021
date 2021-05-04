from django.contrib import admin
from .models import BBCNews, NikkeiNews

# Register your models here.
admin.site.register(BBCNews)
admin.site.register(NikkeiNews)