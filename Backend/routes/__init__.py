from .faq_routes import faq_routes

def init_routes(app, mongo):
    faq_routes(app, mongo)