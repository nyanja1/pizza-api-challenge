
# 🍕 Pizza Restaurant API

A RESTful API for managing restaurants and pizzas using Flask and SQLAlchemy. This API supports basic CRUD operations and associations between restaurants and the pizzas they serve.

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/nyanja1/pizza-api-challenge.git
   cd pizza-api-challenge
   ```

2. **Set up a virtual environment with Pipenv**

   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell
   ```

3. **Set environment variable and initialize database**

   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

4. **Seed the database**

   ```bash
   python server/seed.py
   ```

---

## 🧩 Models

### Restaurant

* `id`: Integer, primary key
* `name`: String, required
* `address`: String, required
* **Relationships**: has many `RestaurantPizzas` (cascading delete)

### Pizza

* `id`: Integer, primary key
* `name`: String, required
* `ingredients`: String, required
* **Relationships**: has many `RestaurantPizzas`

### RestaurantPizza

* `id`: Integer, primary key
* `price`: Integer, required (1–30)
* `restaurant_id`: ForeignKey → Restaurant
* `pizza_id`: ForeignKey → Pizza
* **Relationships**: belongs to both Restaurant and Pizza

---

## 📡 Routes Summary

### 📍 GET `/restaurants`

**Returns**: List of all restaurants
**Example Response**:

```json
[
  { "id": 1, "name": "Kiki's Pizza", "address": "123 Main St" },
  ...
]
```

---

### 📍 GET `/restaurants/<int:id>`

**Returns**: A single restaurant and its pizzas
**Success Response**:

```json
{
  "id": 1,
  "name": "Kiki's Pizza",
  "address": "123 Main St",
  "restaurant_pizzas": [
    { "id": 1, "price": 10, "pizza_id": 1, ... },
    ...
  ]
}
```

**If not found**:

```json
{ "error": "Restaurant not found" }
```

Status: `404`

---

### 🗑️ DELETE `/restaurants/<int:id>`

**Deletes**: A restaurant and all its associated RestaurantPizzas
**Success**: `204 No Content`
**If not found**:

```json
{ "error": "Restaurant not found" }
```

Status: `404`

---

### 📍 GET `/pizzas`

**Returns**: List of all pizzas
**Example**:

```json
[
  { "id": 1, "name": "Margherita", "ingredients": "Tomato Sauce, Mozzarella, Basil" },
  ...
]
```

---

### ➕ POST `/restaurant_pizzas`

**Creates**: A new RestaurantPizza
**Request**:

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Success Response** (`201 Created`):

```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato Sauce, Mozzarella, Basil"
  },
  "restaurant": {
    "id": 2,
    "name": "Luigi's Pizzeria",
    "address": "456 Oak Ave"
  }
}
```

**Error Responses**:

* Missing fields:

  ```json
  { "errors": ["Missing required fields"] }
  ```

  Status: `400`

* Invalid price:

  ```json
  { "errors": ["Price must be between 1 and 30"] }
  ```

  Status: `400`

---

## ✅ Validation Rules

* `RestaurantPizza.price` must be between **1** and **30**.
* All fields in POST requests must be provided.
* Cascading delete is enforced: deleting a restaurant removes associated `RestaurantPizzas`.

---

## 🧪 Testing with Postman

1. Open Postman
2. Click Import
3. Upload the file: `challenge-1-pizzas.postman_collection.json`
4. Test each route by running the saved requests.

