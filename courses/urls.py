from django.urls import path
from .views import(
	CourseView,
	CourseListView,
	MyList,
	CourseCreateView,
	CourseUpdateView,
	CourseDeleteView
	)

app_name = 'courses'

urlpatterns = [
	path('demo/',CourseView.as_view(template_name = 'courses/hell.html'), name = 'course-list'),
	path('',CourseListView.as_view(), name = 'course-list'),
	path('<int:id>/',CourseView.as_view(),name = 'detail-view'),
	path('mylist/',MyList.as_view(), name = 'course-list'),
	path('create/',CourseCreateView.as_view(), name = 'create-view'),
	path('<int:id>/update/',CourseUpdateView.as_view(), name = 'update-view'),
	path('<int:id>/delete/',CourseDeleteView.as_view(), name = 'delete-view'),
]