from django.db import models
from django.forms import ModelForm

class Button1(models.Model):
    b1= models.FloatField(
    verbose_name='Input for Button1'
    )

class Button1Form(ModelForm):
    class Meta:
        model=Button1
        fields='__all__'

class Button2(models.Model):
    b2= models.FloatField(
    verbose_name='Input for Button2'
    )

class Button2Form(ModelForm):
    class Meta:
        model=Button2
        fields='__all__'
# Create your models here.
