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