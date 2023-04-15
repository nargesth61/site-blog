from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import registerform ,Userlogin
from django.http import HttpResponse


def signup_user(request ,*args, **kwargs):
    user=request.user
    if user.is_authenticated:
        return HttpResponse(f"you are already register with"+ str(user.email))
    context={}
    if request.POST:
            form=registerform(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email').lower()
                password = form.cleaned_data.get('password1')
                account = authenticate(email = email ,password = password)
                login(request,account)

                return redirect('/')
            else:
                context['registration_form']=form 
    else:
        form = registerform()
        context['registration_form'] = form 
    
    return render(request,'accounts/signup.html',context)


def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("/")

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = Userlogin(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect("/")

	else:
		form = Userlogin()

	context['login_form'] = form

	return render(request, "accounts/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')    




def repassword_user(request):
    pass