from django.db import models
from django.forms import ModelForm

#class temp_input(models.Model):
#    cel_input = models.FloatField()

#class temp_input_form(ModelForm):
#    class Meta:
#        model = temp_input
#        fields = '__all__'

# defining the page input for AD phosphorus calculation
class phos_input(models.Model):
    #x = models.FloatField(verbose_name=' random variable, x > 0')
    #theta = models.FloatField(verbose_name=' scale parameter, theta > 0')
    #k = models.FloatField(verbose_name=' shape paramter, k > 0')
    blood = models.FloatField()
    fish_by = models.FloatField()
    paper_pulp = models.FloatField()
    ob = models.FloatField()
    gt = models.FloatField()
    manure = models.FloatField()

class phos_input_form(ModelForm):
    class Meta:
        model = phos_input
        fields = '__all__'
