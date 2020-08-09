from django import forms

from .models import Course


class CourseModelForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			'course_name',
			'course_instructor',
			'course_duration'
		]