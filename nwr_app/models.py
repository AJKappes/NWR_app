from django.db import models
from django.forms import ModelForm

class temp_input(models.Model):
    cel_input = models.FloatField()

class temp_input_form(ModelForm):
    class Meta:
        model = temp_input
        fields = '__all__'

