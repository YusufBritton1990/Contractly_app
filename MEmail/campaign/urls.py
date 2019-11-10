"""MEmail URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('retrieve', views.campaign_retreive_all),
    path('new-campaign', views.campaign_creation),
    path('update-campaign', views.campaign_update),
    path('campaign-content', views.campaign_content),

    path('get-template', views.get_template),
    path('template-content', views.template_content),
]
