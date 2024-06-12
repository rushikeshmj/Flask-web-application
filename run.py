from app import create_app
from werkzeug.urls import url_quote

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
