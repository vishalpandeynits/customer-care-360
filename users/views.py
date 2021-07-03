from django.shortcuts import render, redirect
from .forms import ProfileForm, SignUpForm
from .models import Profile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile = ProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user = form.save(commit=False)
            user.save()
            Profile.objects.create(user = user, user_type = request.POST.get('user_type'))
            return redirect('login')
    else:
        form = SignUpForm()
        profile = ProfileForm()
    params = {
        'signupform': form,
        'profileform':profile
        }
    return render(request, 'registration/signup.html', params)