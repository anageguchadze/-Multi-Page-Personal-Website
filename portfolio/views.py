from django.shortcuts import render, redirect

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        return redirect("success")
    return render(request, 'contact.html')

def success_view(request):
    return render(request, 'success.html')