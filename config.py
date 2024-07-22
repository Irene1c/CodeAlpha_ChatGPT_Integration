"""Configuration"""
import os


class ConfigClass:
    SECRET_KEY = os.getenv('SECRET_KEY')
