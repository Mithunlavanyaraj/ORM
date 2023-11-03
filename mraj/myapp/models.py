from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    name=models.CharField(max_length=100)
    numberofmatch=models.IntegerField()
    age=models.IntegerField()
    height=models.IntegerField()
    salary=models.IntegerField()

class footballplayerAdmin(admin.ModelAdmin):
    list_display=('name','numberofmatch','age','height')
