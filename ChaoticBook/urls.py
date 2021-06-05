from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

from .appConfig import APP_NAME

urlpatterns = [
    path(
        "", include_docs_urls(title=APP_NAME, description="v1.0", public=True)
    ),
    path("accounts/", include("Accounts.urls")),
    path("profiles/", include("Profiles.urls")),
    path("posts/", include("Posts.urls")),
    path("comments/", include("Comments.urls")),
    path("likes/", include("Likes.urls")),
    path("follows/", include("Follows.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
