"""smarthr URL Configuration

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
# from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.urls import path, include
from django.conf import settings
from material.admin.sites import site

urlpatterns = [
    path('', include('core.urls')),
    path('i18n/', include('django.conf.urls.i18n')), # < here
    # path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('questions/', include('questions.urls')),
    path('services/', include('services.urls')),
    path('who/', include('our_team.urls')),
    #Path del admin
    path('admin/', include('material.admin.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Personalizacion del admin
site.site_header = ('SmartHR Admin Portal')
site.site_title = ('SmartHR Admin')
site.index_title = ('SmartAdmin')
site.favicon = staticfiles('core/images/logo-positivo.png') 