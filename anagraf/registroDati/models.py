from django.db import models

from tagging.fields import TagField
from tagging.models import Tag  

import datetime

#import tagging

# Create your models here.

class Subject(models.Model):

	# nome
	name = models.CharField(max_length=64)

	# telefono
	phone_number = models.CharField(max_length=30)

	# email
	email = models.EmailField(blank='')

	# eta
	birthdate = models.DateField()

	# cv allegato
	cv = models.FileField(
                upload_to='/home/alessandro/Documenti',
                null=True, blank=True
        )

        locations = TagField()
        skills = TagField()
        targets = TagField()
    
        note = models.TextField(blank='')

        @property
        def age(self):
            date = datetime.datetime.now().date().year - self.birthdate.year
            return date

        def __unicode__(self):
             #return "%s, %s" %(self.name,self.email)
             return self.name
              
        def get_tags(self):
            return Tag.objects.get_for_object(self) 

	
class Activity(models.Model):

	# nome
	name = models.CharField(max_length = 30)

	# descrizione
	description = models.CharField(max_length = 30)
	
	def __unicode__(self):
            return self.name

class ContactResult(models.Model):

	# soggetto
	subject = models.ForeignKey(Subject)

	# attivita
	activity = models.ForeignKey(Activity)

	# timestamp
	timestamp = models.DateTimeField(auto_now = True)

	# notes
	notes = models.CharField(max_length = 256)

	def __unicode__(self):
            return "%s, %s" %(self.timestamp, self.notes)
                    
