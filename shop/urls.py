from django.urls import path
from .views import HomePage, Catalog, Marketing

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('marketing/', Marketing.as_view(), name="marketing")
]
