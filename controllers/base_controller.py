from bottle import static_file, request

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def set_session(self, key, value):
        request.environ['beaker.session'][key] = value
        request.environ['beaker.session'].save()

    def get_session(self, key, default=None):
        return request.environ['beaker.session'].get(key, default)

    def _setup_base_routes(self):
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def serve_static(self, filename):
        return static_file(filename, root='./static')

    def render(self, template, **context):
        from bottle import template as render_template
        return render_template(template, **context)

    def redirect(self, path, code=302):
        from bottle import HTTPResponse, response as bottle_response
        bottle_response.status = code
        bottle_response.set_header('Location', path)
        return bottle_response
