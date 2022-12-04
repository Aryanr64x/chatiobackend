
from django.contrib import admin
from django.urls import path, include
from chattest import socketurls
from users import urls
from chat import chaturls
from django.conf.urls.static import static
from django.conf import settings

...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(urls)),
    path('api/chat', include(chaturls)),
    path('api', include(socketurls))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
