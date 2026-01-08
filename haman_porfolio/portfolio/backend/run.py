from app import create_app
from app.models import db
import os


app = create_app()

# Create tables if they don't exist
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {"message": "Welcome to Hamman Muraya's Portfolio API"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
