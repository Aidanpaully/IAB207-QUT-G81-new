from flask import Flask
from EventBuddyPro import create_app, db  # Import create_app and db

app = create_app()

app.secret_key = '1234567'

# No need to create db instance here; it's already created in create_app

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()

# Hey!