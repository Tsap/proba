class StatMiddleware(object):
	def process_request(self,request): 
		from proba.Profile.models import Stat
		from datetime import datetime
		self.stat = Stat(
			date = datetime.now(),
			request_url = request.META.get('PATH_INFO', None),
			referer_url = request.META.get('HTTP_REFERER', None),
			client_address = request.META.get('REMOTE_ADDR', None),
			agent = request.META.get('HTTP_USER_AGENT', None),
			)
		self.stat.save()
		return None
	
	def process_response(self,request,response):
		from django.template import Context, loader
		from proba.Profile.models import Stat
		stat_view = Stat.objects.all().order_by('-date')[:10]
		t = loader.get_template('statmidleware.html')
		c = Context({'stat_view': stat_view,})
		response.content = response.content.replace('<a name=statistic></a>', t.render(c))
		return response