from django.urls import path, include
from .admin import *

urlpatterns = [
    path("admin/", include("mainapp.urls.admin")),
]
