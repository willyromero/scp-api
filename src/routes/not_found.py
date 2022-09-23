from flask import render_template


def page(err):
    return render_template("not_found_page.html"), 404
