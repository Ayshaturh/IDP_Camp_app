from django.shortcuts import render, redirect
from django.conf import settings

from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Child, Donation , AdoptionRequest
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomPasswordResetForm, CustomSetPasswordForm, DonationForm, AdoptionRequestForm

def child_list(request):
    children = Child.objects.all()
    return render(request, 'base/child_list.html', {'children': children})

def send_donation_email(user, amount):
    subject = 'Thank you for your donation'
    message = f'Dear {user.first_name}, \n\n Thank you for your generous donation of ₦{amount}. \n\n Best regards, \n IDP App Team'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject,message,email_from, recipient_list)

@login_required
def donation_form(request):
    amount = request.POST.get('amount')
    description = request.POST.get('description')
    donation_type = request.POST.get('donation_type')
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = Donation.objects.create(
                user=request.user,
                description=description,
                donation_type=donation_type,
                amount=amount,
            )
            send_donation_email(request.user, donation.amount)
            return redirect('donations_success')
    else:
        form = DonationForm()
    
    return render(request, 'base/donation_form.html', {'form': form})

def donate(request):
    form = DonationForm()
    amount = request.POST.get('amount')
    description = request.POST.get('description')
    donation_type = request.POST.get('donation_type')
   
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = Donation.objects.create(
                user=request.user,
                description=description,
                donation_type=donation_type,
                amount=amount,
            )
            send_donation_email(request.user, donation.amount)
            return redirect('donations_success')
    return render(request, 'base/donate.html', {'form': form})

def donations_success(request):
    return render(request, 'base/donations_success.html')

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def blog(request):
    return render(request, 'base/blog.html')


@login_required
def adoption_request(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.user = request.user
            adoption_request.child = child
            adoption_request.save()
            return redirect('child_list')
    else:
        form = AdoptionRequestForm()
    return render(request, 'create_adoption_request.html', {'form': form, 'child': child})

@login_required
def adoption_requests_view(request):
    user_requests = AdoptionRequest.objects.filter(user=request.user)
    return render(request, 'base/adoption_requests.html', {'adoption_requests': user_requests})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'base/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserLoginForm()
    return render(request, 'base/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'base/password_reset.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'base/password_reset_confirm.html'





