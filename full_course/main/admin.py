from django.contrib import admin
from .models import RoomDatabase
# Register your models here.


class RoomDatabaseView(admin.ModelAdmin):
    list_display = ("name", "description", "updated", "created")


admin.site.register(RoomDatabase, RoomDatabaseView)
