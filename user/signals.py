# In your views.py
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.shortcuts import redirect

def profiled_view(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile doesn't exist
        return redirect('create-profile')  # Or show a message to create a profile
    return render(request, 'user/profiled.html', {'profile': profile})
