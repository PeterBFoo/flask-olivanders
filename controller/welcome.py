from app import app


class Welcome:

    @app.route('/user/<name>')
    def index(name):
        return "<h1>Welcome to Olivanders, {}!</h1>".format(name)
