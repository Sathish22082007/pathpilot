from django.urls import path
from .views import home, dashboard, analyze


urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("api/analyze/", analyze, name="analyze"),
]
