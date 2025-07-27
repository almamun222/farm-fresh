
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('product/', include('product.urls')),
    path('contact', views.contact, name='contact'),
    path('detail', views.detail, name='detail'),
    path('feature', views.feature, name='features'),
    path('service', views.service, name='service'),
    path('team', views.detail, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
     path('customer/', include('customer.urls')),


]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
