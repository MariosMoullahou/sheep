from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("new/", views.sheep_create, name="sheep_create"),
    path("<int:pk>/", views.sheep_detail, name="sheep_detail"),
    path("lamping/",views.lamping, name="lamping"),
    path("milking/",views.milking, name="milking"),
]
