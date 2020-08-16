# -*- coding: utf-8 -*-
from flask import jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.models.book import Book
from app.validators.forms import BookSearchForm


api = Redprint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    books = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()
    # books = [book.hide('summary', 'id') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)