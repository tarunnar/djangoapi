"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restapp import views as restview
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("gen/", restview.CustomerViewSet)
customer_list_view = restview.CustomerViewSet.as_view({
    "get": "list",
    "post": "create"
})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.EmployeeList.as_view()),
    path('api/<int:empid>/', views.Employeeparticular.as_view()),
    path('restapi/<int:id>/', restview.CustomerView.as_view()),
    path('restapi/', restview.CustomerView.as_view()),
    path('genericapi/<int:custid>/', restview.GenericCustomerView.as_view()),
    path('genericapi/', restview.GenericCustomerView.as_view()),

    path('api/v1/auth/login', restview.LoginView.as_view()),
    path('api/v1/auth/logout/', restview.LogoutView.as_view()),
    path("gen/", include(router.urls))


]
