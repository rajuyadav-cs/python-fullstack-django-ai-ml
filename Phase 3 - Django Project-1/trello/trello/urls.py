from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from views import Home


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", Home.as_view(), name="home"),

    path("", include("accounts.urls")),
    path("", include("teams.urls")),

    path("projects/", include("projects.urls")),
    path("tasks/", include("tasks.urls")),

    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)