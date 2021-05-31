from django.urls import path
from .views import (HomePage, Catalog, Marketing,
                    view_policy, create_policy, policy_update, profile)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('policy/', view_policy, name='policy'),
    path('profile/', profile, name='profile'),
    path('create-policy', create_policy, name='create-policy'),
    path('policy/<id>/update/', policy_update, name='update-policy'),
    path('marketing/', Marketing.as_view(), name="marketing")
]
