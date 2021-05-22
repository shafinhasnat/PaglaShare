from flask import Flask, send_file, request

class Server:
	def __init__(self):
		self.app = Flask(__name__)
		@self.app.route("/", methods=['GET', 'POST'])
		def index():
			file = open('.file', 'r')
			try:
				return send_file(file.read(), as_attachment=True)
				print("success")
			except:
				print("error")
				return "Make sure you have selected your file to share in PaglaShare-Desktop"