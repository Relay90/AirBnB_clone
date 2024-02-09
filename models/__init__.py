#!/usr/bin/python3
"""Initialization of the FileStorage instance"""

from models.engine.file_storage import FileStorage

def initialize_storage():
    """Initialize FileStorage instance and reload data."""
    storage = FileStorage()
    storage.reload()

if __name__ == "__main__":
    initialize_storage()
