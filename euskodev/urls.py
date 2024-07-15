from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.i18n import i18n_patterns
from applications import home
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('applications.home.urls')),  # Reemplaza 'yourapp' por tu aplicación real
)