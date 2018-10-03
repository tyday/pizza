"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# copied code from mozillas Django tutorial
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path("", include("orders.urls")),
    path("admin/", admin.site.urls),
]
# i dont think i want this
# path('', RedirectView.as_view(url='/orders')

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#Add Django site authentication urls ( for login, logout, password management)
urlpatterns += [ path('accounts/', include('django.contrib.auth.urls')),]

