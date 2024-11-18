from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomSignUpForm
from .forms import ProfileEditForm  

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to home page or desired page
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'user/login.html', {'form': form})

@login_required
def profile_edit(request):
    profile = request.user.profile  # Assuming a one-to-one link between User and UserProfile
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            # Update profile fields
            profile.bio = form.cleaned_data['bio']
            profile.save()
            
            # Update user fields (like username or email)
            request.user.username = form.cleaned_data['username']
            request.user.email = form.cleaned_data['email']
            request.user.location = form.cleaned_data['location']
            request.user.save()

            return redirect('profile')  # Redirect after successful update
    else:
        form = ProfileEditForm(initial={
            'username': request.user.username,
            'email': request.user.email,
            'bio': profile.bio,
            'location': profile.location,
        })

    return render(request, 'user/profile.html', {'form': form})


@login_required
def profiled_view(request):
    profiled = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'user/profiled_view.html', {'profile': profiled})


def custom_signup_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomSignUpForm()

    return render(request, 'user/signup.html', {'form': form})


