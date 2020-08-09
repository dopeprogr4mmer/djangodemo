from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

from .forms import DemoForm, RawProductForm

# Create your views here.
def demo_view(request, *args, **kwargs):
	#obj = Demo.objects.get(id=1)
	return render(request, "index.html", {})


def demo_create_view(request, *args, **kwargs):
	form = DemoForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DemoForm()

	context = {
		'form':form
	}
	return render(request, "demoapp/product_create.html", context)



def product_create_view(request):
	my_form = RawProductForm()
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
		"form" : my_form
	}
	return render(request, "demoapp/product_create.html", context)


def dynamic_url_demo(request, my_id):
	#obj = Demo.objects.get(id=id)
	obj = get_object_or_404(Product, id=my_id)
	context = {
		"object":obj
	}

	return render(request,"demoapp/product_details.html", context)


def product_delete(request, id):
	obj = get_object_or_404(Product, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../../')
	context = {
		"object":obj
	}
	return render(request,"demoapp/product_delete.html", context)


def list_view(request):
	queryset = Product.objects.all()
	template = 'demoapp/list_view.html'
	context = {
	"object_list":queryset
	}
	return render(request, template, context)