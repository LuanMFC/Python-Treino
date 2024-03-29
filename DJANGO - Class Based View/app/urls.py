"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarListRender, NewCar, DetailsViewCars
from users.views import new_user, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_user/', new_user, name="new_user"),
    path('login/', user_login, name="user_login"),
    path('logout', user_logout, name='logout'),
    path('cars/', CarListRender.as_view(), name="cars_list"),
    path('new_car/', NewCar.as_view(), name="new_car"),
    path('cars/<int:pk>/', DetailsViewCars.as_view(), name="details_car")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
