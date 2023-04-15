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
    path("index",views.index,name='index'),
    
    path("AIF",views.AIF,name='AIF'),
    path("CFFF",views.CFFF,name='CFFF'),
    path("CIS",views.CIS,name='CIS'),
    path("KMDY",views.KMDY,name='KMDY'),
    path("Krishi",views.Krishi,name='Krishi'),
    path("MAS",views.MAS,name='MAS'),
    path("NMOEO",views.NMOEO,name='NMOEO'),
    path("NMONF",views.NMONF,name='NMONF'),
    path("PMFBY",views.PMFBY,name='PMFBY'),
    path("PMKSN",views.PMKSN,name='PMKSN'),
    path("PMKSY",views.PMKSY,name='PMKSY'),
]
