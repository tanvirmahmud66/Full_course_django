from django.forms import ModelForm
from .models import RoomDatabase


class RoomForm(ModelForm):
    class Meta:
        model = RoomDatabase
        fields = '__all__'
