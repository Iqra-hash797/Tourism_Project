
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.Login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logOut, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('tickets/', views.tickets, name='tickets'),
    path('bahrain/', views.bahrain, name='bahrain'),
    path('abudhabi/', views.abudhabi, name='abudhabi'),
    path('riyadh/', views.riyadh, name='riyadh'),
    path('qatar/', views.qatar, name='qatar'),
    path('kuwait/', views.kuwait, name='kuwait'),
    path('saudiarabia/', views.saudiarabia, name='saudiarabia'),
]
