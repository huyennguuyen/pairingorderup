from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table 

with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)

    beverages   = MenuItemType(name="Beverages")
    entrees     = MenuItemType(name="Entrees")
    sides       = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French Fries", price=3.50, type=sides, menu=dinner)
    drp   = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    db.session.add_all( [beverages, entrees, sides, dinner, fries, drp, jambalaya] )

    for i in range(1,11):
        table = Table(number=i, capacity=4) 
        db.session.add(table)

    db.session.commit()
