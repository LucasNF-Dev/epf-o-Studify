# app.py
from bottle import Bottle, TEMPLATE_PATH # Importe TEMPLATE_PATH
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        
        # ⚠️ AJUSTE CRUCIAL: Configura o caminho de busca dos templates do Bottle
        # O Bottle usa uma lista, então adicionamos o caminho da nossa config.
        # TEMPLATE_PATH é importado do bottle para fazer este ajuste.
        TEMPLATE_PATH.insert(0, self.config.TEMPLATE_PATH) 
        
        print(f"✅ Template Path configurado para: {TEMPLATE_PATH[0]}")


    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        # A função init_controllers está em controllers/__init__.py
        init_controllers(self.bottle)


    def run(self):
        self.setup_routes()
        print(f"Servidor Studify iniciado em http://{self.config.HOST}:{self.config.PORT}")
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()