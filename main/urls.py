from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('info/', views.about, name='info'),
    path('contacts/', views.contacts, name='contacts'),
    path('blog/', views.blog, name='blog'),
    path('ourwork/', views.ourwork, name='ourwork'),
    path('download/', views.download, name='download'),
]
