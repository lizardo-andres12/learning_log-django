from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank user registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log user in and redirect to home page

            login(request, new_user)
            return redirect('learning_logs:index')

    # Display blank form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
