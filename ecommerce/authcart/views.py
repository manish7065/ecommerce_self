from django.shortcuts import render,redirect




# Create your views here.
def signup(request):
    return render(request,"authentication/signup.html")

def handlelogin(request):
    """
    Logs the user into their account.

    This view takes a request object as an argument and renders the login.html template.
    """
    return render(request,"authentication/login.html") 

def handlelogout(request):
    """
    Logs the user out of their account.

    This view takes a request object as an argument and renders the logout.html template.
    """
    return redirect('/authcart/login')   

    