"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from demoapp import views as demo_views
#from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contact.urls')),
    path('blogs/', include('blog.urls')),
    path('courses/',include('courses.urls')),
    path('',demo_views.demo_view, name = 'demo_view'),
    path('create/', demo_views.demo_create_view, name = 'demo_create_view'),
    #path('contact/', contact_views.contact_view, name = 'contact_view'),
    path('create1/', demo_views.product_create_view, name = 'create_view1'),
    path('products/<int:my_id>/', demo_views.dynamic_url_demo, name = 'actual-use'),
    path('products/<int:id>/delete/', demo_views.product_delete, name = 'delete'),
    path('product_list/', demo_views.list_view, name = "list_views"),
]