from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
	CreateView,
	UpdateView,
	DetailView,
	ListView,
	DeleteView
	)

from .forms import ContactModelForm

from .models import Contact

def contact_view(request, *args, **kwargs):
	context = {}
	template = 'contact.html'
	return render(request,template,context)

class ContactCreateView(CreateView):
	template_name = "contact/contact_create.html" 	#overriding generic    
	form_class = ContactModelForm
	queryset = Contact.objects.all()			#<blog>/<modelname>_list.html
	#success_url = '/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	#def get_success_url(self):
	#	return '/'

class ContactListView(ListView):
	template_name = "contact/contact_list.html" 	#overriding generic 
	queryset = Contact.objects.all()

class ContactDetailView(DetailView):
	template_name = "contact/contact_detail.html" 	#overriding generic    
	#queryset = Contact.objects.filter(id__gt = 2)   #more with querysets

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Contact, id = id_)


class ContactUpdateView(UpdateView):
	template_name = "contact/contact_create.html" 	#overriding generic    
	form_class = ContactModelForm
	queryset = Contact.objects.all()			#<blog>/<modelname>_list.html
	#success_url = '/'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Contact, id = id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ContactDeleteView(DeleteView):
	template_name = "contact/contact_delete.html" 	#overriding generic    
	#queryset = Contact.objects.filter(id__gt = 1)   #more with querysets

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Contact, id = id_)

	def get_success_url(self):
		return reverse('contacts:contact-list')



# Create your views here.
