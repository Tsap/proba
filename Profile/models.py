from django.db import models

class Contact_type (models.Model):
	name_contact_type = models.CharField(max_length=20)
	def __unicode__(self):
		return self.name_contact_type
		
class Person (models.Model):
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	bio = models.DateField()
	def __unicode__(self):
		return self.name

class Contact (models.Model):
	id_contact_type = models.ForeignKey(Contact_type)
	id_user = models.ForeignKey(Person)    
	value_contact = models.CharField(max_length=50)
	def __unicode__(self):
		return self.value_contact	

class Stat (models.Model):
        date = models.DateTimeField(auto_now_add=True)
        request_url = models.CharField(max_length=500)
        referer_url = models.URLField(verify_exists=False, blank=True, null=True)
        client_address = models.IPAddressField(blank=True, null=True)
        agent = models.TextField(null=True,blank=True)
    	def __unicode__(self):
			return '%s %s ' % (self.date, self.client_address)