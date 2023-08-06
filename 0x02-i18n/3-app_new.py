#!/usr/bin/env python3
"""
    Basic flask setup using babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel()


class Config:
    """ class Configuration for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale() -> str:
    """
    get the best matched language for the locale
    Returns:
        str: language short form
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    The index/home page
    Returns:
        str: renders the template for display
    """
    title: str = _("home_title")
    header: str = _("home_header")
    return render_template('./1-index.html', title=title, header=header)


if __name__ == "__main__":
    app.run()
