from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('webapp.urls')),
    path('about/', include('webapp.urls')),
    path('items/', include('webapp.urls')),
    path('signin/', include('webapp.urls')),
    path('signout/', include('webapp.urls')),
    path('signup/', include('webapp.urls')),
    path('profile/', include('webapp.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)