from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
    TokenVerifyView
)


urlpatterns = (
    path('api/v1/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/api/v1/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/api/v1/', TokenVerifyView.as_view(), name='token_verify'),
)
