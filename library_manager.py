from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response
from app import app, db
from app.routes import book
from app.models import Author, Book, Shelf

app = Flask(__name__)

@app.route("/")
def add_book():
    book.add_book()
   

