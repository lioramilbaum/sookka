#!/usr/bin/env python3

from flask import render_template


def configure_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')
