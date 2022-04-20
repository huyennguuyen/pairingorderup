from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Employee

with app.app_context():
    # db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()