import tornado.ioloop,tornado.web,tornado.escape,tornado.options,tornado.websocket
from tornado.options import define, options
import os,string,random,json,base64
define("port", default=8080, type=int)
options.parse_command_line()
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            autoescape="xhtml_escape",
            debug=True,
            )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    def post(self):
        print (self.get_argument("dataURL"))
        with open(self.get_argument("imageName")+".png","w") as pic:
            pic.write(base64.b64decode(self.get_argument("dataURL")))
def main():
    tornado.options.parse_command_line()
    Application().listen(options.port)
    print("Waked!")
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()
