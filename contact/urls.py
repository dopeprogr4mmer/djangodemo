from django.urls import path
from . import views
from .views import(
	ContactCreateView,
	ContactUpdateView,
	ContactDetailView,
	ContactListView,
	ContactDeleteView,
	contact_view
	)

app_name = 'contacts'

urlpatterns = [
	path("",ContactListView.as_view(), name = 'contact-list'),
	path("create/",ContactCreateView.as_view(), name ='contact-create'),
	path("<int:id>/", ContactDetailView.as_view(), name = 'contact-detail'),
	path("<int:id>/update", ContactUpdateView.as_view(), name = 'contact-update'),
	path("<int:id>/delete", ContactDeleteView.as_view(), name = 'contact-delete'),
	path("bingo/", contact_view, name = 'bingo' )
]