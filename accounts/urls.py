from django.urls import path
from .views import SignUp, include

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
]