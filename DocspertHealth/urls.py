from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('transfer_accounts.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="DocspertHealth",
        default_version='api-v1',
        description="API v1 docs",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@quran.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-v1'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui-v1'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]
