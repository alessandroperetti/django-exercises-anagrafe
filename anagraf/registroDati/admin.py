from registroDati.models import Subject #import Subject table
from registroDati.models import Activity#import Activity table
from registroDati.models import ContactResult
from django.contrib import admin


admin.site.register(Subject)
admin.site.register(Activity)
admin.site.register(ContactResult)




