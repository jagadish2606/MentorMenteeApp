from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SignupView, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
