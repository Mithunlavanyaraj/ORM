# Ex02 Django ORM Web Application
## Date: 31/10/2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
Admin.py 

from django.contrib import admin
from .models import footballplayer,footballplayerAdmin
admin.site.register(footballplayer,footballplayerAdmin)

Models.py

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


```

## OUTPUT
![image](https://github.com/Mithunlavanyaraj/ORM/assets/120077786/9407db1a-2f6f-4fb1-a830-3dd4d1f0c42d)


## RESULT
Thus the program for creating a database using ORM has been executed successfully
