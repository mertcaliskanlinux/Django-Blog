
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('about/',TemplateView.as_view(template_name='about.html')),
    path('contact/',include('contact.urls')),
]
