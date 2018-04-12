import yaml
#import pdb
from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def authenticate(username):
    with open("users.yaml","r") as f:
        userslist = yaml.load(f)
    	print userslist 
        for users_k, users_v in userslist.items():
	    print users_k
	    print users_v
            for user_name, user_pass in users_v.items():
	        print user_name
		print user_pass               
		if user_name == username:
		    print "in if : %s" %user_name 
                    #pdb.set_trace()
		    return user_pass


@app.route('/')
@auth.login_required
def hello():
    return "Hello %s!" %auth.username()


if __name__ == '__main__':
   app.run()

