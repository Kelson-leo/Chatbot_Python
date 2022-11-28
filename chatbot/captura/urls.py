from django.urls import admin
from .views import capturas 

urlpatterns = [

        path('<int:code_user>/', capturas)
  
       

 ]
