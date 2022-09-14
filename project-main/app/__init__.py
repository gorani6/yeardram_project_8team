from flask import Flask

app = Flask(__name__)

# noqa (app dependents)
from app import views, sample_page