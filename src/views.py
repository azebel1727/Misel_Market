from django.shortcuts import render, redirect
from .models import ArtItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import ArtItem

# SHOWCASE: This is your Main Service Page
def upload_art(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        price = request.POST.get('price')
        image_file = request.FILES.get('image_file') # Get the actual file
        
        ArtItem.objects.create(
            title=title, 
            artist_name=artist, 
            price=price, 
            image=image_file # Save the file
        )
        return redirect('dashboard')
    return render(request, 'upload.html')

# DELETE: The "Control" Action
def delete_art(request, art_id):
    item = get_object_or_404(ArtItem, id=art_id)
    item.delete()
    return redirect('dashboard')
def login_page(request):
    if request.method == 'POST':
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')

        # Check if the user exists in the database by email
        try:
            # In Django's default User model, we store the email in 'username' or 'email'
            # Here, we search for a user whose email matches the input
            user_obj = User.objects.get(email=email_input)
            
            # Authenticate using the username (which Django needs) and password
            user = authenticate(request, username=user_obj.username, password=password_input)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid password. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "This email is not registered. Please sign up first.")

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password_input != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')

        # Check if email is already taken
        if User.objects.filter(email=email_input).exists():
            messages.error(request, "Email already registered. Please login.")
            return redirect('login')

        # Create user: We use email as the 'username' to keep Django happy
        user = User.objects.create_user(username=email_input, email=email_input, password=password_input)
        user.save()
        
        messages.success(request, "Registration successful! You can now login.")
        return redirect('login')

    return render(request, 'register.html')

# This MUST be named gallery_dashboard to match your urls.py
def gallery_dashboard(request):
    items = ArtItem.objects.all()
    return render(request, 'dashboard.html', {'items': items})

# This MUST be named buy_art to match your urls.py
def buy_art(request, art_id):
    try:
        item = ArtItem.objects.get(id=art_id)
        item.status = "Sold"
        item.save()
    except ArtItem.DoesNotExist:
        pass
    return redirect('dashboard')