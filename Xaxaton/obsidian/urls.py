from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendors/', include('applications.vendor.urls')),
    path('cart/', include('applications.cart.urls')),
    path('', include('applications.core.urls')),
    path('', include('applications.product.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
