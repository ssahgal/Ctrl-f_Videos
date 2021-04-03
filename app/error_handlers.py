from app import app

from flask import render_template, request


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def server_error(e):

    app.logger.error(f"Server error: {e}, route: {request.url}")

    return render_template('500.html')

@app.errorhandler(403)
def forbidden(e):

    app.logger.error(f"Forbidden error: {e}, route: {request.url}")

    return render_template('403.html')