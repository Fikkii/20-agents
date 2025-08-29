from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignupForm, LoginForm

from .models import CustomUser


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful! You are now logged in.")
            return redirect("dashboard")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")  # Django still uses "username" field internally
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                email = CustomUser.objects.get(email = email).email
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("dashboard")
        messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out successfully.")
    return redirect("login")

def home_view(request):
    return render(request, "home.html")

# Example data (replace with DB query later)
AGENTS = [
    {"name": "Content Creator", "description": "Brainstorm, write, and generate social media contents", "link": "/agents/content-creator"},
    {"name": "Resume Creator", "description": "Generate your perfect Resume as a Job seeker", "link": "/agents/resume-creator"},
    {"name": "Researcher", "description": "The perfect agent, for analyst who will like to jumpstart their research", "link": "/agents/researcher"},
    {"name": "SEO Optimizer", "description": "Get Noticed by search engines with this amazing tool", "link": "/agents/seo-optimizer"},
    {"name": "Social Media Campaign", "description": "Generate Campaign for your Social Media Influencing", "link": "/agents/smedia-campaign"},
    # ... add all 20 agents
]




@login_required(login_url="/login")
def dashboard_view(request):
    return render(request, "dashboard.html", {
        "agents": AGENTS
    })
