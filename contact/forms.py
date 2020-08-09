from django import forms

from .models import Contact

class ContactModelForm(forms.ModelForm):
	name = forms.CharField(required = True, max_length = 100)
	mobile_no = forms.IntegerField(
					required = True,
					widget = forms.Textarea(
						attrs = {
							'placeholder':'enter your 10 digit mobile number',
							'rows':1,
							'cols':15
							}
						)
		)
	email = forms.EmailField()
	address = forms.CharField(
					widget = forms.Textarea(
						attrs = {
							'placeholder':'your-description',
							'class':'new-class-name',                                                       
							'id':'my-id-for-textarea',
							'rows':10,
							'cols':120
							}
						)
		)


	class Meta:
		model = Contact
		fields = [
			'name',
			'mobile_no',
			'email',
			'address'
		]


	def clean_mobile_no(self, *argss, **kwargs):
		mobile_no = self.cleaned_data.get("mobile_no")
		if mobile_no > 999999999:
			return mobile_no
		raise forms.ValidationError("The Mobile Number Is Not Valid")
		


