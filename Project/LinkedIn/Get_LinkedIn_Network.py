from linkedin import linkedin

API_KEY = '783fh7yras3my8'
CLIENT_SECRET = 'AE9pir3x4fJj6gsh'


authentication = linkedin.LinkedInAuthentication(API_KEY, CLIENT_SECRET, RETURN_URL, linked
print authentication.authorization_url

application = linkedin.LinkedInApplication(authentication)
application
