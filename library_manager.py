from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response
from app import app, db
from app.routes import book
from app.models import Author, Book, Shelf

def addbook(book):
    book.add_book(title=book)
   

addbook("Book1")


