from django.contrib import admin
from django.urls import path
from emp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.HomePage,name='home'),
    path("about/",views.AboutUS,name='about'),
    path("services/",views.Services,name='services'),
    path("addemp/",views.Add_emp,name='addemp'),
    path("edit/<int:id>/",views.Editemp,name='edit'),
    path("delete/<int:id>/",views.Deleteemp,name='delete'),
    path('default/', views.default, name='default'),
    path('accounts/login/', views.loginView, name='login'),
    path('accounts/signup/', views.signupView, name='signup'),
    path('accounts/logout/', views.logoutView, name='logout')
]