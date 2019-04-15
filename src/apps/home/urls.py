from django.urls import path
from .views import home, LoginView, logOut

app_name = 'home'


urlpatterns = [
    path('', home, name='home_page'),
    path('logout/', logOut, name='logout_page'),
    path('login/', LoginView.as_view(), name='login_page'),
]
