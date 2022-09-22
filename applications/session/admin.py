from django.contrib import admin
from .models import Session,TimeSession,Series
# Register your models here.
admin.site.register(Session)
admin.site.register(TimeSession)
admin.site.register(Series)