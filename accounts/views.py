from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from contacts.models import Contact

def register(request):
	
	if request.method == 'POST':
		# REGISTER USER LOGIC
		
		# Get form values
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']
		
		# Check if passwords match
		if password != password2:
			messages.error(request, 'Password mismatch')
			return redirect('register')
		
		# Check if username is available
		elif User.objects.filter(username=username).exists():
			messages.error(request, 'Username taken')
			return redirect('register')
			
		# Check if email is available
		elif User.objects.filter(email=email).exists():
			messages.error(request, 'Email taken')
			return redirect('register')
		
		# Looks good
		else: 
			user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
			# Login after register
			''' # auto login
			auth.login(request, user)
			messages.success(request, 'You are now logged in')
			return redirect('index')
			'''
			user.save();
			messages.success(request, 'You are now registered')
			return redirect('login')
			
		return redirect('register')
	
	else:
		return render(request, 'accounts/register.html')
	
def login(request):
	
	#DEBUG
	#print('LOGIN')
	#print(pretty_request(request))
	
	if request.method == 'POST':
		# LOGIN USER LOGIC

		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username, password=password)
		
		if user:
			auth.login(request, user)
			messages.success(request, 'You are now logged in')
			return redirect('dashboard')
		else:
			
			messages.error(request, 'Invalid credentials')
			return redirect('login')
	else:
		return render(request, 'accounts/login.html')

# DEBUG
def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )

def logout(request):
	
	#DEBUG
	#print('views.logout called')
	#print(pretty_request(request))
	#return redirect('about')
	
	if request.method == 'POST':
		# LOGOUT USER LOGIC
		auth.logout(request)
		messages.success(request, 'You are now logged out')
		return redirect('index')
	else:		 
		return redirect('index')
	
def dashboard(request):
	
	user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
	
	context = {
	
		'contacts': user_contacts
	
	}
	return render(request, 'accounts/dashboard.html', context)
	
