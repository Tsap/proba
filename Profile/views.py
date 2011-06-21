from django.shortcuts import render_to_response
from Profile.models import *

def Welcome(request):
	account_data = Person.objects.all()
	contact_data = Contact.objects.all()
	return render_to_response('Profile/welcome.html', {'account_data': account_data, 'contact_data': contact_data})
