from django.db import models
from django.forms import ModelForm

#class temp_input(models.Model):
#    cel_input = models.FloatField()

#class temp_input_form(ModelForm):
#    class Meta:
#        model = temp_input
#        fields = '__all__'

# defining the page input for pdf calculation
class pdf_input(models.Model):
    x = models.FloatField(verbose_name=' random variable, x > 0')
    theta = models.FloatField(verbose_name=' scale parameter, theta > 0')
    k = models.FloatField(verbose_name=' shape paramter, k > 0')

class pdf_input_form(ModelForm):
    class Meta:
        model = pdf_input
        fields = '__all__'
