from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

auth = HTTPBasicAuth()

@auth.get_password
def get_pw(username):
	file = open("usersList.txt","r")

	users = file.readlines()

	print users
	
	file.close()

	for user in users:
		print  user
                values = user.split('=',1)
     		print values
		if (values[0] == username):
			return values[1].strip('\n')
	return None

@app.route('/')
@auth.login_required
def login():
	return "Welcome %s!!!" %auth.username()

if __name__ == '__main__':
	app.run()
