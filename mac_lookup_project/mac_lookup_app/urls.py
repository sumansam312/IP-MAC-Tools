from django.urls import path
from . import views

urlpatterns = [
    path("mac_lookup/", views.mac_lookup, name="mac_lookup"),
    path("subnetting/", views.subnetting, name="subnetting"),
    path("dashboard/", views.dashboard, name="dashboard"),  # Changed path
    path("", views.mac_lookup, name="home"),
]
