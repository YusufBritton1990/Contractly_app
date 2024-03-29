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
    path('retrieve', views.list_retreive_all),
    path('partial', views.list_retreive_partial),

    path('seg/retrieve', views.segment_retreive_all),

    path('mer/retrieve', views.merge_retreive_all),

    path('mem/retrieve', views.members_retreive_all),
    path('mem/one', views.members_retreive_one),
    path('mem/update', views.members_update),

]
