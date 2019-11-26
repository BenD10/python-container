import falcon

class HelloWorldResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_OK
        resp.body = 'Hello World!'

app = falcon.API()
app.add_route('/', HelloWorldResource())
