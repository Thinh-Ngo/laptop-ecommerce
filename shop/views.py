from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from marketing.models import PotentialClient
from .models import Help, PolicyContent, Unit
from .forms import PolicyForm
from clients.forms import ClientForm
from .forms import HelpForm


def view_policy(request):
    policy = PolicyContent.objects.filter(
        is_valid=True).order_by('-start_date')[0]
    context = {
        'policy': policy
    }
    return render(request, "policy_page.html", context)


def contact_page(request):
    form = HelpForm
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            message = data['message']

            contact = Help()
            contact.email = email
            contact.message = message
            contact.save()

            messages.success(
                request, 'Thank you for reaching out, we connect you soon...')
            form = HelpForm()
            context = {
                'form': form,
            }
        else:
            context = {
                'form': form,
            }
        return render(request, 'contact.html', context)
    else:
        form = HelpForm()

    context = {'form': HelpForm}
    return render(request, 'contact.html', context)


@login_required
def create_policy(request):
    title = 'create post'
    form = PolicyForm(request.POST or None, request.FILES or None)
    author = request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect("policy")
    context = {
        'form': form,
        'title': title
    }
    return render(request, "create_policy.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        p_form = ClientForm(
            request.POST, request.FILES, instance=request.user
        )
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f"You account has been updated")
            return redirect("profile")

    else:
        p_form = ClientForm(instance=request.user)

    client = request.user
    context = {
        "client": client,
        "p_form": p_form,
        "title": "profile"
    }
    return render(request, "profile.html", context)


@login_required
def policy_update(request, id):
    title = 'Update'
    post = get_object_or_404(PolicyContent, id=id)
    form = PolicyForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author = request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("policy"), kwargs={
                'id': form.instance.id
            })
    context = {
        'title': title,
        'form': form
    }
    return render(request, "create_policy.html", context)


class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')


class Catalog(ListView):
    template_name = 'catalog.html'
    model = Unit


class Marketing(View):
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
