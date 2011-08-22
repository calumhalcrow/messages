from os import path as op
import logging

import tornado.web
import tornadio
import tornadio.router
import tornadio.server

ROOT = op.normpath(op.dirname(__file__))

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class MessageConnection(tornadio.SocketConnection):

#    def on_open(self, *args, **kwargs):
#        self.send("Welcome from the server.")

#    def on_message(self, message):
#        # Pong message back
#        self.send(message)

MessageRouter = tornadio.get_router(MessageConnection)

application = tornado.web.Application(
    [(r"/", IndexHandler), MessageRouter.route()],
    flash_policy_port = 843,
    flash_policy_file = op.join(ROOT, 'flashpolicy.xml'),
    socket_io_port = 8001
)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    tornadio.server.SocketServer(application)
