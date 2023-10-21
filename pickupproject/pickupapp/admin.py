from django.contrib import admin

from .models import ScheduleModel,PlaceModel,MemberModel
# Register your models here.

admin.site.register(ScheduleModel)

admin.site.register(PlaceModel)

admin.site.register(MemberModel)