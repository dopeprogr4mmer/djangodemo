from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length = 120)
	price = models.DecimalField(decimal_places = 2, max_digits = 100)
	description = models.TextField(blank = True, null = True)
	summary = models.TextField() 
	featured = models.BooleanField(default = True)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("actual-use", kwargs={"my_id":self.id})   #f"/products/{self.id}/"
