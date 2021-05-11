import falcon


class Hola:
    def on_get(self, request, response):
        data = {
            "laboratorio": 1
        }
        response.media = data


api = falcon.API()
api.add_route('/saludo', Hola())
