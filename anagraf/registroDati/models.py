from django.db import models

# Create your models here.

class Subject(models.Model):

	# nome
	name = models.CharField(max_length=30)

	# cognome
	surname = models.CharField(max_length=30)

	# telefono
	phone_number = models.CharField(max_length=30)

	# email
	email = models.EmailField()

	# eta
	age = models.IntegerField()

	# cv allegato
	cv = models.FilePathField(path = "/")

	# territori
	# competenze
	# target
	# note
	def __unicode__(self):
	        return self.question
	
class Activity(models.Model):

	# nome
	name = models.CharField(max_length = 30)

	# descrizione
	description = models.CharField(max_length = 30)
	
	def __unicode__(self):
	        return self.question

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
	        return self.question	
