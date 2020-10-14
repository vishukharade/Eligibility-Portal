from django.contrib import admin
from myapp.models import Students,Aptitude,Technical
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=("id","name","gender","email_id","phone_no","password","college","branch","year","div","role")
admin.site.register(Students,StudentAdmin)     

class AptitudeAdmin(admin.ModelAdmin):
    list_display=("id","Question","optionA","optionB","optionC","optionD","correct")
admin.site.register(Aptitude,AptitudeAdmin) 

class TechnicalAdmin(admin.ModelAdmin):
    list_display=("id","Question","optionA","optionB","optionC","optionD","correct")
admin.site.register(Technical,TechnicalAdmin) 