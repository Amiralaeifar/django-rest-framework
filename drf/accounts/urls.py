from django.urls import path 
from . import views 
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]


# UserViewSet urls 
router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls