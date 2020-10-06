import tornado.web
import tornado.ioloop
from database_connect import sqldb


class registerRequestHandler(tornado.web.RequestHandler):

    def get(self):
        
        self.render("register.html")

    def post(self):
        fname = self.get_argument('fname',"")
        lname = self.get_argument('lname',"")
        position = self.get_argument('positon',"")
        email = self.get_argument('email')
        pas = self.get_argument('password',"")
        phone= self.get_argument('phone',"")

        sqldb.registration(fname,lname,email,pas,phone,position)
        
        self.write("all done")
class loginRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        email = self.get_argument('email',"")
        password = self.get_argument('password',"")

        self.write("email " +email+" password "+password)

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("loginpage.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/register", registerRequestHandler),
        (r"/", listRequestHandler),
        (r"/login", loginRequestHandler)
    ])
    
    port = 8877
    app.listen(port)
    print("Application is ready and listening on port {}".format(port))
    tornado.ioloop.IOLoop.current().start()
