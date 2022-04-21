from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
metadata_obj = MetaData()

order_items = db.Table(
    "order_items",
    metadata_obj,
    db.Column( "id", db.Integer, primary_key=True),
    db.Column( "order_id", db.Integer, db.ForeignKey("orders.id"), nullable=False ),
    db.Column( "menu_item_id", db.Integer, db.ForeignKey("menu_items.id"), nullable=False )
)


class Employee(db.Model, UserMixin): 
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property 
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    items = db.relationship("MenuItem", back_populates="menu", cascade="all, delete")


class MenuItem(db.Model):
    __tableName__ = "menu_items"

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(50), nullable=False)
    price   = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey("menus.id"), nullable=False)
    menu_type_id = db.Column(db.Integer, db.ForeignKey("menu_item_types.id"), nullable=False)

    menu = db.relationship("Menu", back_populates="items")
    type = db.relationship("MenuItemType", back_populates="items")
#    orders = db.relationship("Order", back_populates="items", secondary=order_items)

class MenuItemType(db.Model):
    __tablename__ = "menu_item_types"

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(20), nullable=False)

    items   = db.relationship("MenuItem", back_populates="type", cascade="all, delete")


class Table(db.Model):
    __tablename__ = "tables"

    id       = db.Column(db.Integer, primary_key=True)
    number   = db.Column(db.Integer, nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)


class Order(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    table_id    = db.Column(db.Integer, db.ForeignKey("tables.id"), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False) 
    closed      = db.Column(db.Boolean, nullable=False)

    items = db.relationship("MenuItem", back_populates="orders", secondary=order_items)
