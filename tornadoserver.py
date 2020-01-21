import tornado.ioloop
import tornado.web



#serves html form data to the webpage localhost:8881/1
class Main_Handler(tornado.web.RequestHandler):
    def get(self):
        
        self.render("index1.html", title="MyTitle")
#recieves the form data from /1 and posts a response on /2


class Submit_Handler(tornado.web.RequestHandler):
    def post(self):
        text1 = self.get_argument(name="mytextarea")
        choice1 = self.get_argument(name = "mychoice1")
        choice2 = self.get_argument(name = "mychoice2")
        
        self.render("poll_submit.html",text=text1, name1=choice1, name2=choice2)
    get = post

class Vote_Handler(tornado.web.RequestHandler):
    def post(self):
        self.render("Vote_Submit.html")
    get = post
class Update_Handler(tornado.web.RequestHandler):
    def post(self):
        update1 = self.get_argument(name = "mytextarea")
        update2 = self.get_argument(name = "mychoice1")
        update3 = self.get_argument(name = "mychoice2")
        self.render("update.html",U1=update1,U2=update2,U3=update3)
    get = post
        


    

if __name__ == "__main__":
    app = tornado.web.Application([
        
        (r"/", Main_Handler),
        (r"/2", Submit_Handler),
        (r"/3", Vote_Handler),
        (r'/4', Update_Handler)
       
       
    ])
    app.listen(9999)
    print("I'm listening on port 9999")
    tornado.ioloop.IOLoop.current().start()