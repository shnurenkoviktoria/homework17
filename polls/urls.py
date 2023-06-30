from django.urls import path

from . import views

urlpatterns = [
    path("", views.form_image, name="forms"),
    path("images/", views.images_show, name="show"),
]