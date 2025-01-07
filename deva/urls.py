from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL for the homepage
    path('submit/', views.data, name='submit'),  # URL for form submission 
    path('db/', views.view, name='db'),  # URL for viewing the database
    path('delete/', views.delete, name='delete'),
    path('form/', views.form, name='form'),
    path('submit_details/', views.submit_details, name='submit'),
    path('submit/submit_details/', views.submit_details, name='submit'),
   
    ]
