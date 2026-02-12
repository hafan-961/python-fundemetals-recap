from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import  Column, Integer, String, Float, ForeignKey, text
from sqlalchemy.orm import  sessionmaker, relationship

engine = create_engine("sqlite:///fintrack.db")
base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Category(base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    expenses = relationship("Expense", back_populates="category")

class Expense(base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Integer)
    date = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")

class Subscription(base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)
    next_date = Column(String)

class Budget(base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True)
    month = Column(String)
    limit = Column(Integer)

base.metadata.create_all(engine)

def add_category():
    name = input("Category name: ")
    session.add(Category(name=name))
    session.commit()
    print("Category added")

def add_expense():
    title = input("Expense title: ")
    amount = int(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    category_id = int(input("Category ID: "))
    session.add(Expense(title=title, amount=amount, date=date, category_id=category_id))
    session.commit()
    print("Expense added")

def update_expense():
    eid = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == eid).first()
    if expense:
        expense.title = input("New title: ")
        expense.amount = int(input("New amount: "))
        expense.date = input("New date: ")
        session.commit()
        print("Expense updated")
    else:
        print("Expense not found")

def delete_expense():
    eid = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == eid).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted")
    else:
        print("Expense not found")

def search_by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    expenses = session.query(Expense).filter(Expense.date == date).all()
    if expenses:
        print(f"Expenses on {date}:")
        for e in expenses:
            print(f"{e.title} - ₹{e.amount} ({e.category.name})")
    else:
        print("No expenses found for this date")

def add_subscription():
    name = input("Subscription name: ")
    amount = float(input("Amount: "))
    next_date = input("Next payment date (YYYY-MM-DD): ")
    session.add(Subscription(name=name, amount=amount, next_date=next_date))
    session.commit()
    print("subscription added")

def view_subscriptions():
    subscriptions = session.query(Subscription).all()
    if subscriptions:
        print("active subscriptions:")
        for s in subscriptions:
            print(f"{s.name} - ₹{s.amount}/month (Next: {s.next_date})")
    else:
        print("No subscriptions found")

def category_analytics():
    sql = """
    SELECT categories.name, SUM(expenses.amount)
    FROM categories
    JOIN expenses ON categories.id = expenses.category_id
    GROUP BY categories.name
    """
    result = session.execute(text(sql))
    print("Category Wise Spending Report")
    for row in result:
        print(row[0] , "-" , row[1])

def set_budget():
    month = input("Month (YYYY-MM): ")
    limit = int(input("Budget limit: "))
    session.add(Budget(month=month, limit=limit))
    session.commit()
    print(" Monthly budget set")

def budget_alert():
    month = input("Month (YYYY-MM): ")
    total = session.execute(
        text("SELECT SUM(amount) FROM expenses WHERE date LIKE :m"),
        {"m": f"{month}%"}
    ).scalar()
    budget = session.query(Budget).filter(Budget.month == month).first()
    if budget:
        if total and total > budget.limit:
            print(f"Budget exceeded! Spent: ₹{total} | Limit: ₹{budget.limit}")
        else:
            spent = total if total else 0
            remaining = budget.limit - spent
            print(f" Within budget Spent: ₹{spent} | Remaining: ₹{remaining}")
    else:
        print("No budget set for this month")

def view_categories():
    categories = session.query(Category).all()
    if categories:
        print(" Available Categories:")
        for c in categories:
            print(f"ID: {c.id} - {c.name}")
    else:
        print("No categories found")

while True:
    print("""
===== HAFAN FINTRACK PRO =====
1. Add Category
2. View Categories
3. Add Expense
4. Update Expense
5. Delete Expense
6. Search Expense by Date
7. Add Subscription
8. View Subscriptions
9. Category Analytics
10. Set Monthly Budget
11. Budget Alert
12. Exit
""")
    choice = input("Choose: ")
    if choice == "1":
        add_category()
    elif choice == "2":
        view_categories()
    elif choice == "3":
        add_expense()
    elif choice == "4":
        update_expense()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        search_by_date()
    elif choice == "7":
        add_subscription()
    elif choice == "8":
        view_subscriptions()
    elif choice == "9":
        category_analytics()
    elif choice == "10":
        set_budget()
    elif choice == "11":
        budget_alert()
    elif choice == "12":
        print("Thank you for using FinTrack pro")
        break
    else:
        print("Invalid choice")



# ---------------------------------- README ---------------------------------------------
# FinTrack Pro

'''FinTrack Pro** is a simple command-line expense tracker built using **Python, SQLAlchemy, and SQLite**.  
It lets users manage categories, expenses, subscriptions, and monthly budgets.

## Features
- Add & view categories
- Add, update, delete expenses
- Search expenses by date
- Track subscriptions
- Category-wise spending report
- Set monthly budget & alerts

## Run the Project
```bash
python main.py
'''