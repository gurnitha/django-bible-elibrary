# app/accounts/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.http import HttpResponse

# Create your views here.

def register_view(request):
	# If the user is not authenticated
	if not request.user.is_authenticated:
		# If the request is POST, then check
		# the inputs from the form fields
		# NOTE: the form input has attributes of:
		# - name:first_name
		# - name:last_name
		# - name:username
		# - name:password1
		# - name:password2
		# NOTE: the form attributes are based on the
		#       attributes of the DEFAULT USER MODEL
		#       pre-define by Django import from
		#       django.contrib.auth.models.
		if request.method=="POST":
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			username = request.POST['username']
			email = request.POST['email']
			password1 = request.POST['password1']
			password2 = request.POST['password2']

			# If password1=password2, then check if
			# the user already exists in the db
			if password1 == password2:
				if User.objects.filter(username=username).exists():
					# If the username already exists
					messages.info(request, 'username is taken, choose another!')
					return redirect('accounts:register')

					# If the user is not exists, check its email
				elif User.objects.filter(email=email).exists():
					messages.info(request, 'Email is taken, choose another!')
					return redirect('accounts:register')

				# If the username and email not exists, the create user
				else:
					user = User.objects.create_user(
						username=username, 
						password=password1,
						email=email, 
						first_name=first_name, 
						last_name=last_name)
					user.save()
					return HttpResponse('Successfull.')
			# If password1!=password2, show the message
			# and redirect the user to the register page.
			else:
				messages.info(request, 'Password didn\'t match')
				return redirect('accounts:register')

	return render(request, 'accounts/register.html')
