from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import restaurant, pizza, restaurant_pizza
from controllers import restaurants_bp, pizzas_bp, restaurant_pizzas_bp

app.register_blueprint(restaurants_bp)
app.register_blueprint(pizzas_bp)
app.register_blueprint(restaurant_pizzas_bp)

if __name__ == '__main__':
    app.run(debug=True)