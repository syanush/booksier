from app import app, db, User, Book


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Book': Book}
