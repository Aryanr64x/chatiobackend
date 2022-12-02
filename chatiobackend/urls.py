
from django.contrib import admin
from django.urls import path, include
from chattest import socketurls
from users import urls
from chat import chaturls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(urls)),
    path('api/chat', include(chaturls)),
    path('api', include(socketurls))
]
