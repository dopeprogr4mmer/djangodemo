from django import forms

from .models import Product

class DemoForm(forms.ModelForm):
	title = forms.CharField(label = 'g')
	email = forms.EmailField()
	price = forms.DecimalField(initial = 199.99)
	description  = forms.CharField(
						required = False,
						widget = forms.Textarea(
								attrs = {
									'placeholder':'your-description',
									'class':'new-class-name',                                                       
									'id':'my-id-for-textarea',
									'rows':20,
									'cols':120
								}
								)
							)

	class Meta:
		model = Product
		fields = [
			'title',
			'price',
			'description'
		]


	def clean_email(self, *argss, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith(".com"):
			raise forms.ValidationError("This is not a valid email")
		return email 




class RawProductForm(forms.Form):
	title = forms.CharField(label = 'g')
	price = forms.DecimalField(initial = 199.99)
	description  = forms.CharField(
						required = False,
						widget = forms.Textarea(
								attrs = {
									'placeholder':'your-description',
									'class':'new-class-name',                                                       
									'id':'my-id-for-textarea',
									'rows':20,
									'cols':120
								}
								)
							)
		
