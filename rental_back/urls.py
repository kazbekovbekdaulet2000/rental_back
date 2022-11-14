from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

schema_view = get_schema_view(
    openapi.Info(
        title="Yume Rental API",
        default_version='v1',
        description="desc",
        contact=openapi.Contact(email="kazbekov.bekdaulet2000@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('product.urls')),
    path('v1/', include('article.urls')),
    path('v1/auth/', include('user.urls')),
    path('v1/manager/', include('manager.urls')),

    # ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # Swagger
    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/swagger/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    path('docs/swagger/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
