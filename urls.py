from django.urls import path
from mysite import views

urlpatterns = [
 path('', views.index, name='index'),
 # path('products', views.products, name='products'),
 # path('gallery', views.gallery, name='gallery'),
 # path('jobs', views.jobs, name='jobs'),
 # path('about', views.about, name='about'),

]

