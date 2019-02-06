from django.shortcuts import render, redirect
from django.contrib.auth import login as signin, logout as log_out, authenticate
from django.contrib.auth.decorators import login_required

from users.forms import LoginForm, SignupForm, UpdateProfileForm

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['user']
			signin(request, user)
			if 'next' in request.GET:
				next = request.GET['next']
				return redirect(next)
			return redirect('index')
	
	else:
		form = LoginForm()

	return render(
		request=request,
		template_name='users/login.html',
		context = {
			'form': form,
		}
	)

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST, request.FILES)		
		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user:
				signin(request, user)
				return redirect('index')

			return redirect('login')

	else:
		form = SignupForm()

	return render(
		request=request,
		template_name='users/signup.html',
		context= {
			'form': form,
		}
	)

@login_required
def logout(request):
	log_out(request)
	return redirect('index')

@login_required
def update_profile(request):
	context = {}
	if request.method == 'POST':
		form = UpdateProfileForm(request.POST, request.FILES)
		if form.is_valid():
			if 'password' in form.cleaned_data:
				password = form.cleaned_data['password']
				user = request.user
				user.set_password(password)
				user.save()

				signin(request, user)
				context['success_message'] = 'Password has changed correctly!'

			if 'picture' in form.cleaned_data:
				picture = form.cleaned_data['picture']
				profile = request.user.splitter
				profile.picture = picture
				profile.save()
				if 'success_message' in context:
					context['success_message'] = 'Profile picture and password correctly saved!'
				else:
					context['success_message'] = 'Profile picture has been saved!'

	else:
		form = UpdateProfileForm()

	context['form'] = form
 
	return render(request, 'users/update_profile.html', context)