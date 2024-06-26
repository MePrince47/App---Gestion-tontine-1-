"""projet_tp URL Configuration

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
from tontine import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page ,name = "Homepage"),
    path('tontine/',views.add_show ,name = "Add"),
    path('tontine/delete/<int:id>',views.suppression ,name = "deletedata"),
    path('tontine/<int:id>/',views.modifier, name = "modifierdata"),
    
    path('membre/',views.add_show_membre ,name = "Add_membre"),
    path('membre/delete/<int:id>',views.suppression_membre ,name = "deletedata_membre"),
    path('membre/<int:id>/',views.modifier_membre, name = "modifierdata_membre"),
]
 