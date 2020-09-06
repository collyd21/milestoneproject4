from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_comps, name='comps'),
    path('<int:comp_id>/', views.comp_info, name='comp_info'),
    path('add/', views.add_comp, name='add_comp'),
    path('edit/<int:comp_id>/', views.edit_comp, name='edit_comp'),
]