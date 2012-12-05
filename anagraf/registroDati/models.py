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
            return 3

        def __unicode__(self):
             return self.name
              
        def get_tags(self):
            return Tag.objects.get_for_object(self) 

        # territori
	# competenze
	# target
	# note
       #def __unicode__(self):
       #    return self.name
	
class Activity(models.Model):

	# nome
	name = models.CharField(max_length = 30)

	# descrizione
	description = models.CharField(max_length = 30)
	
#	def __unicode__(self):
#	        return self.question

class ContactResult(models.Model):

	# soggetto
	subject = models.ForeignKey(Subject)

	# attivita
	activity = models.ForeignKey(Activity)

	# timestamp
	timestamp = models.DateTimeField(auto_now = True)

	# notes
	notes = models.CharField(max_length = 256)

#	def __unicode__(self):
#	        return self.question	
