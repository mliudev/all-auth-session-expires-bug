from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        context = {
            'session_id': request.session.session_key,
            'session_expires': request.session.get_expire_at_browser_close(),
            'session_expiry_date': request.session.get_expiry_date()
        }
        return render(request, self.template_name, context)