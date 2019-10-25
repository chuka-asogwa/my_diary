from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms import RegistrationForm

def register(request):
    """ Register a new user. """
    if request.method != 'POST':
        # Display blank registration form
        form = RegistrationForm()
    else:
        # Process completed form
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user and redirect to home page
            login(request, new_user)
            return redirect('notes:index')
        
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

