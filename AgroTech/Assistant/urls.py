from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('supplier/login/', views.supplier_login, name='supplier_login'),
    path('farmer/login/', views.farmer_login, name='farmer_login'),
    path('admin/login/', views.admin_login, name='admin_login'),
]
