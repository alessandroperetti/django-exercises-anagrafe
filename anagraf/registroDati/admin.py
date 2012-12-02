from registroDati.models import Subject #import Subject table
from registroDati.models import Activity#import Activity table
from registroDati.models import ContactResult
from django.contrib import admin

class SubjectAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'age', 'phone_number', 'email']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Activity)
admin.site.register(ContactResult)




