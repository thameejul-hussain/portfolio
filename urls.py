from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name= "index"),
    path("post/<str:post_id>",views.detail, name= "detail"),
    path("username/",views.username, name= "username"),
    path("new_url",views.new_url, name= "new_url"),
    path("old_url",views.old_url, name= "old_url"),
]

