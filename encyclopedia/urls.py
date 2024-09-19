from django.urls import path

from . import views

app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.ShowPage, name="ShowPage"),
    path("search/", views.search, name="search"),
    path("CreatePage/", views.CreatePage, name="CreatePage"),  
    path("edit/", views.edit , name="edit"),  
    path("ConfirmEdit/", views.ConfirmEdit , name="ConfirmEdit"),  
    path("RandomPage/", views.RandomPage , name="RandomPage"),  
]
