from django.db import models

from django.urls import reverse

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length = 100)
	mobile_no = models.IntegerField(null = False, blank = False)
	email = models.EmailField()
	address = models.TextField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("contacts:contact-detail", kwargs = {"id":self.id})



