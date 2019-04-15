from django.urls import path
from .views import AccountView

app_name = 'account'

urlpatterns = [
    path('<slug:slug>/', AccountView.as_view(), name='account_page'),
]
