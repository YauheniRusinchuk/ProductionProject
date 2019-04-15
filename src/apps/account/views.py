from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from src.models.accounts.models import Account


class AccountView(DetailView):
    template_name   = 'account/index.html'
    queryset        = Account.objects.all()


    def get_object(self):
        slug_    = self.kwargs.get('slug')
        return get_object_or_404(Account, slug=slug_)
