from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_review, name='add_review'),
    path('', views.all_reviews, name='all_reviews'),
]
