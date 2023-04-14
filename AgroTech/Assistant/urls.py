from django.contrib import admin
from django.urls import path
#from . import views
from Assistant import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    #path('admin/login/', views.admin_login, name='admin_login'),
    path("signup",views.signup,name='signup'),
    path("signin",views.signin,name='signin'),
    path("signout",views.signout,name='signout'),
    path("farmerDashboard",views.farmerDashboard,name='farmerDashboard'),
    path("suppliersignup",views.suppliersignup,name='suppliersignup'),
    path("suppliersignin",views.suppliersignin,name='suppliersignin'),
    path("Sppsignout",views.Sppsignout,name='Sppsignout'),
    path("supplier",views.supplier,name='supplier'),
    path("PlaceOrder",views.PlaceOrder,name='PlaceOrder'),
]
