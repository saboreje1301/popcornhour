from app import crear_app
import os

app = crear_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Heroku asigna dinámicamente un puerto
    app.run(host="0.0.0.0", port=port)