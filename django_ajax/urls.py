from django.urls import include, path

from . import views

app_name = "django_ajax"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
]
