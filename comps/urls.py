from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_comps, name='comps'),
    path('<comp_id>', views.comp_info, name='comp_info'),
]