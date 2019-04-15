from django.urls import path
from .views import home, LoginView

app_name = 'home'


urlpatterns = [
    path('', home, name='home_page'),
    path('login/', LoginView.as_view(), name='login_page'),
]
