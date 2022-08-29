"""bikestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
# from bike import views
from bikeapi.models import Bikes
from bikeapi.views import BikesView,BikeDetailsView,BikeModelViews,BikeModelDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/vech/bikes/",BikesView.as_view()),
    path("api/v1/vech/bikes/<int:id>",BikeDetailsView.as_view()),
    path("api/v2/vech/bikes/",BikeModelViews.as_view()),
    path("api/v2/vech/bikes/<int:id>",BikeModelDetailsView.as_view())

]
#bike app
# path("bike/v1/bikes/",views.BikesView.as_view()),
#     path('bike/v1/bikes/<int:id>',views.BikesDetailsView.as_view())