from django.db import models

from django.urls import reverse

# Create your models here.
class Course(models.Model):
	course_name = models.CharField(max_length = 120)
	course_instructor = models.CharField(max_length = 120)
	course_duration = models.DurationField(null = True)
	course_start_time = models.TimeField(null = True)


	def __str__(self):
		return self.course_name


	def get_absolute_url(self):
		return reverse('courses:detail-view',kwargs = {"id":self.id})

