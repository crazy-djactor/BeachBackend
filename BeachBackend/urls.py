"""BeachBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_simplejwt import views as jwt_views
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ====== Token ==========
    path('api/v1/login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('ap1/v1/count_data/', views.PeopleCountUpdate.as_view(), name='count_update')
]