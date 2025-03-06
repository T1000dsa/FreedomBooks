"""
URL configuration for FreedomBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from freedombooks_core import views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('freedombooks_core.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users'))

    # ... the rest of your URLconf goes here ... 
] + debug_toolbar_urls() 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.page_not_found


admin.site.site_header = 'special admin panel'
admin.site.index_title = 'site administration'