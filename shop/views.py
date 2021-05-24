from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from marketing.models import PotentialClient


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        email = request.POST['email']
        try:
            PotentialClient.objects.get(email=email)
            messages.info(request, "You're already subcribed, thanks though.")
            return redirect('home')
        except PotentialClient.DoesNotExist:
            potential_client = PotentialClient()
            potential_client.email = email
            potential_client.save()
            messages.success(
                request, "Thank you for your subscription, now you'll be charge 15$ a month...kidding.")
            return redirect('home')


class Catalog(ListView):
    template_name = 'catalog.html'
