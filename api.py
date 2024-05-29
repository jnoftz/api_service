# from flask import Flask, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

# db = SQLAlchemy(app)
# class Todos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20), nullable=False)
#     body = db.Column(db.String(100))
#     date_added = db.Column(db.DateTime, default=datetime.now)

#     def __repr__(self):
#             return f"Task: {self.title}, Description: {self.title}"


# if __name__ == '__main__':
#     app.run(debug=True)