import facebook
import urllib3

token = ''

class status_publisher(object):
	
	def __init__(self, token):
		self.token = token

	def update(status):
		graph = facebook.GraphAPI(access_token=self.token, version = 2.7)
		

def main():
	status = status_publisher(token)
	

if __name__ == '__main__':
	main()
