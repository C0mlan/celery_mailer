from flask import Flask
from .extensions import celery_init_app
import os
from dotenv import load_dotenv

def create_app():
  load_dotenv()
  app = Flask (__name__)
  app.config["CELERY"] = {   
      "broker_url": "redis://redis:6379/0",
      "result_backend": "redis://redis:6379/0",
      "task_track_started": True
  }
    # Initialize Celery
  celery_init_app(app)