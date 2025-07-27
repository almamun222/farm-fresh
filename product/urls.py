from django.urls import path
from . import views
urlpatterns = [
    path('', views.product,name='product'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('curt/', views.curt,name='curt'),
    path('checkout/', views.checkout,name='checkout'),
    path('submit-order/', views.submit_order, name='submit_order'),
]
