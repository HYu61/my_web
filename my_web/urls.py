"""my_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from my_web.settings import MEDIA_ROOT
from portfolio import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('my_portfolio_admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('projects/', include('projects.urls')),
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),

]

# urlpatterns += static.server(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)