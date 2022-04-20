from flask import Flask
from app.config import Configuration
from app.routes import orders
from app.models import db

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
db.init_app(app)
