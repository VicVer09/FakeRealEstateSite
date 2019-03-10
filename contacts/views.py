from django.shortcuts import render, redirect
from .models import Contact
from listings.models import Listing
from django.contrib import messages
from django.core.mail import send_mail


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



# Create your views here.
def contact(request):
	#print('CONTACT')
	#print(pretty_request(request))
	
	
	if request.method == "POST":
		#print('HELLO')
		listing_id = request.POST['listing_id']
		listing = list(Listing.objects.all().filter(id = listing_id))[0] # savage
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']
	
	''' # not necessary
	def send_inquiry(msg):
		send_mail(
				listing + ' Inquiry',
				'There has been an inquiry for ' + listing + ' from ' + name + ':\n' + message,
				'elmir.verchkovski@mail.mcgill.ca' # this would be dynamic
				)
	'''
	#print(listing)
	#print(request.POST['listing']) # cuts off the rest of the name for some reason
	contact = Contact(listing=listing, listing_id=listing_id , name=name , email=email , phone=phone , message=message , user_id=user_id)
	
	# Check if user has made inquiry already
	if request.user.is_authenticated: 
		has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
		if has_contacted:
			#messages.error(request, 'You have already made an inquiry for this listing, message updated')
			# ^ how to print with an error message for reference
			for old_contact in has_contacted:
				old_contact = contact
				old_contact.save()
			messages.success(request, 'Your inquiry has been updated, a realtor will get back to you soon')
			
			return redirect('/listings/'+listing_id)
	
	contact.save()
	
	messages.success(request, 'Your inquiry has been submitted, a realtor will get back to you soon')

	return redirect('/listings/'+listing_id)
	