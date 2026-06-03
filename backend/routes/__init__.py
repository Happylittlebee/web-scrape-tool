from flask import Blueprint

from .scrape import scrape_bp
from .analyze import analyze_bp
from .download import download_bp

__all__ = ["scrape_bp", "analyze_bp", "download_bp"]