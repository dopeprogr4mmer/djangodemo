from django.shortcuts import render

from .models import Demo

from .forms import DemoForm

# Create your views here.
def demo_view(request, *args, **kwargs):
	obj = Demo.objects.get(id=1)
	return render(request, "demoapp/demo.html", {})


def demo_create_view(request, *args, **kwargs):
	form = DemoForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DemoForm()

	context = {
		'form':form
	}
	return render(request, "demoapp/product_create.html", context)
