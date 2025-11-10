from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_page(request):
    # Redirect already-logged-in users
    if request.user.is_authenticated:
        return redirect('homepage')  # name of your homepage URL

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # log the user in (session-based)
            return redirect('homepage')  # <-- this should redirect to your homepage
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")
# Optional: logout view
def logout_page(request):
    logout(request)
    return redirect('login')
