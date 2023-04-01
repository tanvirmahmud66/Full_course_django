from django.contrib import admin
from .models import RoomDatabase, Topic, Massage
# Register your models here.


class RoomDatabaseView(admin.ModelAdmin):
    list_display = ("host", "topic", "name",
                    "description", "updated", "created")


class MassageView(admin.ModelAdmin):
    list_display = ('user', 'room', 'body', 'updated', 'created')


admin.site.register(RoomDatabase, RoomDatabaseView)
admin.site.register(Topic)
admin.site.register(Massage, MassageView)
