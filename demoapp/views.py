from django.shortcuts import render

from .models import Demo

# Create your views here.
def demo_view(request, *args, **kwargs):
	obj = Demo.objects.get(id=1)
	return render(request, "demoapp/demo.html", {})


