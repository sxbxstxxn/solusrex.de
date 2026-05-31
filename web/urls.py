from django.urls import path

from .views import index, shops, verlag


urlpatterns = [
    path("", index, name="index"),
    path("verlag/", verlag, name="verlag"),
    path("shops/", shops, name="shops"),
]
