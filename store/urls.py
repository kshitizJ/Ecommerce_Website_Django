from django.urls import path

from .views import store

urlpatterns = [
    # Leave as empty string for base url
    path('', store, name="store")
]
