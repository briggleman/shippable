from flask import Flask
from werkzeug.utils import find_modules, import_string


def create_app(config=None):
    app = Flask("shippable")

    app.config.update(dict(
        DEBUG=True,
        SECRET_KEY="i<3cicdsoftware!"
    ))

    app.config.update(config or {})
    app.config.from_envvar("SHIPPABLE_SETTINGS", silent=True)

    register_blueprints(app)

    return app

def register_blueprints(app):
    for name in find_modules("demo.blueprints"):
        mod = import_string(name)
        if hasattr(mod, "bp"):
            app.register_blueprint(mod.bp)
    return None

if __name__ == "__main__":
    app = create_app()
    app.run()