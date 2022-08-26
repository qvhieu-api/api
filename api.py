from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import requests,os
from datetime import *
#os.system("clear")
app = Flask(__name__)
api = Api(app)
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]
@app.route("/")
def main():
	return "Welcome"
@app.route("/book")
def api_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No id field provided. Please specify an id."
	results = []
	for book in books:
		if book['id'] == id:
			results.append(book)
	return jsonify(results)
@app.route("/likepage")
def likepage():
	id = request.args['id']
	ck = request.args['ck']
	head = {"cookie":ck}
	link = requests.get("https://mbasic.facebook.com/"+id,headers=head).url
	b = requests.get(link,headers=head).text
	url = "https://mbasic.facebook.com/a/profile.php?"+b.split('/a/profile.php?')[1].split('"')[0].replace('amp;','')
	like = requests.get(url,headers=head,allow_redirects=False).text
	if like=="":
		now  = datetime.now().strftime("%H:%M:%S")
		print(f"\033[1;33m{now} <> Like Page Success!\033[1;0m")
		return "Like Page Success!"
	elif "Tài khoản của bạn hiện bị hạn chế" in like:
		print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
		return "Tài khoản của bạn hiện bị hạn chế"
	else:
		return like
@app.route("/likepost")
def likepost():
	id = request.args['id']
	ck = request.args['ck']
	head = {"cookie":ck}
	link = requests.get("https://mbasic.facebook.com/"+id,headers=head).url
	b = requests.get(link,headers=head).text
	url = "https://mbasic.facebook.com/a/like.php?"+b.split('/a/like.php?')[1].split('"')[0].replace('amp;','')
	like = requests.get(url,headers=head,allow_redirects=False).text
	if like=="":
		now  = datetime.now().strftime("%H:%M:%S")
		print(f"\033[1;33m{now} <> Like Post Success!\033[1;0m")
		return "Like Post Success!"
	elif "Tài khoản của bạn hiện bị hạn chế" in like:
		print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
		return "Tài khoản của bạn hiện bị hạn chế"
	else:
		return like
@app.route("/sub")
def sub():
	id = request.args['id']
	ck = request.args['ck']
	head = {"cookie":ck}
	link = requests.get("https://mbasic.facebook.com/"+id,headers=head).url
	b = requests.get(link,headers=head).text
	url = "https://mbasic.facebook.com/a/subscribe.php?"+b.split('/a/subscribe.php?')[1].split('"')[0].replace('amp;','')
	like = requests.get(url,headers=head,allow_redirects=False).text
	if like=="":
		now  = datetime.now().strftime("%H:%M:%S")
		print (f"\033[1;33m{now} <> Subscribe Success!\033[1;0m")
		return "Subscribe Success!"
	elif "Tài khoản của bạn hiện bị hạn chế" in like:
		print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
		return "Tài khoản của bạn hiện bị hạn chế"
	else:
		return like
@app.route("/fb")
def fb():
	job = request.args['job']
	id = request.args['id']
	ck = request.args['ck']
	head = {"cookie":ck}
	link = requests.get("https://mbasic.facebook.com/"+id,headers=head).url
	b = requests.get(link,headers=head).text
	if job=="TĂNG LIKE CHO BÀI VIẾT":
		url = "https://mbasic.facebook.com/a/like.php?"+b.split('/a/like.php?')[1].split('"')[0].replace('amp;','')
		like = requests.get(url,headers=head,allow_redirects=False).text
		if like=="":
			now  = datetime.now().strftime("%H:%M:%S")
			print(f"\033[1;33m{now} <> Like Post Success!\033[1;0m")
			return "Like Post Success!"
		elif "Tài khoản của bạn hiện bị hạn chế" in like:
			print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
			return "Tài khoản của bạn hiện bị hạn chế"
		else:
			return like
	elif job=="TĂNG LOVE CHO BÀI VIẾT":
		link = b.split('/reactions/picker/?')[1].split('"')[0].replace('amp;','')
		r = requests.get("https://mbasic.facebook.com/reactions/picker/?"+link,headers=head).text
		s = r.split('/ufi/reaction/?')[2].split('"')[0].replace("amp;","")
		like = requests.get("https://mbasic.facebook.com/ufi/reaction/?"+s,headers=head,allow_redirects=False).text
		if like=="":
			now  = datetime.now().strftime("%H:%M:%S")
			print(f"\033[1;33m{now} <> Love Post Success!\033[1;0m")
			return "Love Post Success!"
		elif "Tài khoản của bạn hiện bị hạn chế" in like:
			print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
			return "Tài khoản của bạn hiện bị hạn chế"
		else:
			return like
	elif job=="TĂNG LIKE CHO FANPAGE":
		url = "https://mbasic.facebook.com/a/profile.php?"+b.split('/a/profile.php?')[1].split('"')[0].replace('amp;','')
		like = requests.get(url,headers=head,allow_redirects=False).text
		if like=="":
			now  = datetime.now().strftime("%H:%M:%S")
			print(f"\033[1;33m{now} <> Like Page Success!\033[1;0m")
			return "Like Page Success!"
		elif "Tài khoản của bạn hiện bị hạn chế" in like:
			print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
			return "Tài khoản của bạn hiện bị hạn chế"
		else:
			return like
	elif job=="TĂNG THƯƠNG THƯƠNG CHO BÀI VIẾT":
		link = b.split('/reactions/picker/?')[1].split('"')[0].replace('amp;','')
		r = requests.get("https://mbasic.facebook.com/reactions/picker/?"+link,headers=head).text
		s = r.split('/ufi/reaction/?')[3].split('"')[0].replace("amp;","")
		like = requests.get("https://mbasic.facebook.com/ufi/reaction/?"+s,headers=head,allow_redirects=False).text
		if like=="":
			now  = datetime.now().strftime("%H:%M:%S")
			print(f"\033[1;33m{now} <> Care Post Success!\033[1;0m")
			return "Care Post Success!"
		elif "Tài khoản của bạn hiện bị hạn chế" in like:
			print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
			return "Tài khoản của bạn hiện bị hạn chế"
		else:
			return like
	elif job=="TĂNG LƯỢT THEO DÕI":
		url = "https://mbasic.facebook.com/a/subscribe.php?"+b.split('/a/subscribe.php?')[1].split('"')[0].replace('amp;','')
		like = requests.get(url,headers=head,allow_redirects=False).text
		if like=="":
			now  = datetime.now().strftime("%H:%M:%S")
			print (f"\033[1;33m{now} <> Subscribe Success!\033[1;0m")
			return "Subscribe Success!"
		elif "Tài khoản của bạn hiện bị hạn chế" in like:
			print ("\033[1;32mTài khoản của bạn hiện bị hạn chế")
			return "Tài khoản của bạn hiện bị hạn chế"
		else:
			return like
	else:
		return "false"
@app.route("/ig")
def ig():
	job = request.args['job']
	url = request.args['url']
	ck = request.args['ck']
	csrftoken = ck.split('csrftoken=')[1].split(';')[0]
	head = {
	"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36",
	"cookie":ck,
	}
	if job=="TĂNG LƯỢT THEO DÕI":
		id = requests.get(url+"/?__a=1",headers=head).text.split('profilePage_')[1].split('"')[0]
		url = f"https://www.instagram.com/web/friendships/{id}/follow/"
	elif job=="TĂNG LIKE CHO BÀI VIẾT":
		id = requests.get(url,headers=head).text.split('content="instagram://media?id=')[1].split('"')[0]
		url = f'https://www.instagram.com/web/likes/{id}/like/'
	else:
		pass
	print(id)
	head = {
	"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36",
	"x-csrftoken":csrftoken,
	"cookie":ck,
	}
	r = requests.post(url,data="",headers=head)
	now  = datetime.now().strftime("%H:%M:%S")
	print(f"\033[1;33m{now} <> {job} Success!\033[1;0m")
	return "ok"
if __name__ == '__main__':
    app.run(debug=True)
