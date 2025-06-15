from server.app import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Kiki's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's Pizzeria", address="456 Oak Ave")
    db.session.add_all([r1, r2])

    p1 = Pizza(name="Margherita", ingredients="Tomato Sauce, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([p1, p2])

    rp1 = RestaurantPizza(price=10, restaurant_id=1, pizza_id=1)
    rp2 = RestaurantPizza(price=12, restaurant_id=1, pizza_id=2)
    rp3 = RestaurantPizza(price=8, restaurant_id=2, pizza_id=1)
    db.session.add_all([rp1, rp2, rp3])

    db.session.commit()
    print("Database seeded!")

if __name__ == '__main__':
    seed_data()