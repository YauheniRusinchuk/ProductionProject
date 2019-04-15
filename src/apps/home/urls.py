from django.urls import path, include
from .views import (
    home,
    LoginView,
    logOut,
    RegisterUser,
)
app_name = 'home'


urlpatterns = [
    path('', home, name='home_page'),
    path('account/', include('src.apps.account.urls', namespace='account')),
    path('register/', RegisterUser.as_view(), name='register_page'),
    path('logout/', logOut, name='logout_page'),
    path('login/', LoginView.as_view(), name='login_page'),
]
