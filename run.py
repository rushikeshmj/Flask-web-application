from app import create_app
from urllib.parse import quote as url_quote

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
