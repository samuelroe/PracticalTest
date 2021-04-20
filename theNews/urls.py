from django.urls import path
from theNews import views

app_name = 'theNews'
urlpatterns = [
    path('', views.index , name = 'index'),
]