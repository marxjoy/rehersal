from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path


urlpatterns = [
	path('', include('reservation.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]