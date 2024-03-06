from django.urls import path, re_path
from .views import HomePageView, RegistrationPageView, LoginPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('sing-up/', RegistrationPageView.as_view(), name='registration'),
    path('sing-in/', LoginPageView.as_view(), name='authentication')

]