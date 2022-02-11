from flask import Flask
from flask_migrate import Migrate

# 1 - Uma das formas
# mg = Migrate()


def init_app(app: Flask):
    # mg.init_app(app=app, db=app.db)
    # 2 - Segunda forma
    Migrate(app=app, db=app.db, compare_type=True)
