from .views import MyTokenObtainPairView
from .views import index, createUser
from django.urls import path


urlpatterns = [

    path('/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', MyTokenObtainPairView.as_view(), name='token_refresh'),
    path('/',index),
    path('/users/create/', createUser),
    # path('/users/profile/create/', )

]