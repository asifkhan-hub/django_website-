from django.contrib import admin
admin.site.site_header = "A.pycoder"
admin.site.index_title = "Welcome to A.pycoder"
admin.site.site_title = "A.pycoder Tutorial"
# Register your models here.
from .models import *
admin.site.register(Contact)
