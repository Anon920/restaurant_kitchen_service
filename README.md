# Restaurant kitchen service

### This is a site that implements a kitchen management service for restaurants.

## Installing / Getting started

### Python3 must be already installed

```shell
git clone https://github.com/Anon920/restaurant_kitchen_service.git
cd restaurant-kitchen-service
```
```shell
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
## Set Up Database
```shell
python manage.py makemigrations
python manage.py migrate
```

## Start the app
```shell
python manage.py runserver
```

At this point, the app runs at http://127.0.0.1:8000/.

## Demo

### DB Structura:

![Restaurant Service](https://github.com/user-attachments/assets/f1cb6441-b4cf-4dc5-87f9-2c8ffcd14b02)

### Home page

![image](https://github.com/user-attachments/assets/c0d4f7f5-6467-434c-a064-2584216e53b5)

### Cook profile

![image](https://github.com/user-attachments/assets/21ed433d-6156-4ec5-89dd-f4934a2fdf4b)

### Cook list

![image](https://github.com/user-attachments/assets/b142acf6-4882-4dd7-bc88-0ee585aa9129)

### Dish list

![image](https://github.com/user-attachments/assets/6743c9b6-b9ae-4494-ba48-5286a0971950)

### Dish Types

![image](https://github.com/user-attachments/assets/414fe1eb-dfbe-4b60-b77d-459f9b66145a)