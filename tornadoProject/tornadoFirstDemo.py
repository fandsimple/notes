#!/usr/bin/python
# -*- coding: utf-8 -*-


import tornado.web
import tornado.ioloop
import logging


class IndexHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        return self.write('<h1>fanding is a good man</h1>')




if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ])

    print('start app ...')
    app.listen(8000)

    tornado.ioloop.IOLoop.current().start()











