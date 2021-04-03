from flask import Flask

app = Flask(__name__)

# Config env by using: export FLASK_APP='{env}'
if app.config["ENV"] == 'production':
    # Using a production configuration
    app.config.from_object("config.ProductionConfig")
else:
    #Using a development configuration
    app.config.from_object("config.DevelopmentConfig")


from app import views
from app import forms
