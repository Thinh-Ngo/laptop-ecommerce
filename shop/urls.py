from django.urls import path
from .views import HomePage, Catalog

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('catalog/', Catalog.as_view(), name='catalog'),
]
