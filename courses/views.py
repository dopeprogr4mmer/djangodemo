from django.shortcuts import render,get_object_or_404,redirect

from django.views import View
# Create your views here.

from .models import Course

from .forms import CourseModelForm
#Base view class = VIEW

class CourseObjectMixin(object):
	model = Course
	#lookup = 'id'

	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, id = id)
		return obj 

class CourseView(View):
	template_name = 'Courses/detail_view.html'
	def get(self, request, id = None, *args, **kwargs):
		#return render(request, self.template_name, {})

		#GET_METHOD
		context = {}
		if id is not None:
			obj = get_object_or_404(Course, id = id)
			context['object'] = obj
		return render(request, self.template_name, context)


class CourseCreateView(View):
	template_name = 'Courses/create.html'
	def get(self, request, *args, **kwargs):
		#return render(request, self.template_name, {})

		#GET_METHOD
		form = CourseModelForm()
		context = {'form':form}
		return render(request, self.template_name, context)
	#POST_METHOD
	def post(self, request, *args, **kwargs):
		form = CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
			form = CourseModelForm()
		context = {'form':form}
		return render(request, self.template_name, context)



class CourseUpdateView(CourseObjectMixin, View):
	template_name = 'Courses/update.html'

	'''def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id = id)
		return obj'''


	#GET_METHOD
	def get(self, request, id = None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(instance = obj)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	#POST_METHOD
	def post(self, request,id = None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(request.POST, instance = obj)
			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)


class CourseDeleteView(CourseObjectMixin, View):
	template_name = 'Courses/delete.html'

	'''def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id = id)
		return obj'''


	#GET_METHOD
	def get(self, request, id = None, *args, **kwargs):
		context = {'object':self.get_object()}
		obj = self.get_object()
		'''if obj is not None:
			form = CourseModelForm(instance = obj)
			context['object'] = obj
			#context['form'] = form'''
		return render(request, self.template_name, context)

	#POST_METHOD
	def post(self, request,id = None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			#context['form'] = form
			return redirect('/courses/')
		return render(request, self.template_name, context)


class CourseListView(View):
	template_name = 'Courses/list_view.html'
	queryset = Course.objects.all()


	def get_queryset(self):
		return self.queryset


	def get(self, request, *args, **kwargs):
		context = {
			'object_list':self.get_queryset()
		}
		return render(request, self.template_name, context)

class MyList(CourseListView):
	queryset = Course.objects.filter(id = 4)



#HTTP Methods
def fn_view(request, *args, **kwargs):
	print(request.method)
	return render(request,'courses/this.html',{})
