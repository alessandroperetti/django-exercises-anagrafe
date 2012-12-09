from registroDati.models import Subject #import Subject table
from registroDati.models import Activity#import Activity table
from registroDati.models import ContactResult
from django.contrib import admin

class SubjectAdmin(admin.ModelAdmin):
   # fields = ('name', 'birthdate', 'cv', 'phone_number', 'email',
   #         'locations', 'skills', 'targets'
   # )
    list_display = ('__unicode__', 'phone_number', 'age', 'email') 
    search_fields = ['__unicode__']
    list_filter = ['locations']

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description')

class ContactResultAdmin(admin.ModelAdmin):
    list_diplay = ('__unicode__')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(ContactResult,ContactResultAdmin)




