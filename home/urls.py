from django.urls import path,include
from . import views
urlpatterns = [
    path('post',views.index,name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('post/<int:id>', views.postdetail, name="postdetail"),
]