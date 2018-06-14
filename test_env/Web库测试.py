# Flask库的测试
from flask import Flask
'''app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

app.run()'''


# Tornado库的测试
import tornado.ioloop
import tornado.web
'''class MainHandler(tornado.web.RequestHandler):
	"""docstring for MainHandler"""
	def get(self):
		self.write("Hello World!")

def make_app():
	return tornado.web.Application([
		(r"/",MainHandler),
	])
	
app = make_app()
app.listen(8888)
tornado.ioloop.IOLoop.current().start()'''
