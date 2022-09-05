from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appGH.urls')),
    # path('calendar/', include('appCalendario.urls')),
]
