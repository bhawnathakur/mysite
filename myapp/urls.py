from django.urls import path,include
from . import views
urlpatterns = [
    path('forms', views.test_form_view,name='testform'),
    path('', views.index,name='index'),
    
]