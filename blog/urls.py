from django.urls import path
from .views import BlogPageView,BlogDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',BlogPageView.as_view(), name='index'), 
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post') #POSTA AİT TEKİL SAYFAYA YÖNLENDİMRE HER POSTA TEK SAYFA OLMASI İÇİN PRİMARY KEY 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   #media kaydetme ve yönlendirme post her projede gerekli 
