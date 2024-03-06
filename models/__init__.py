#!/usr/bin/python3
"""
__init__ file for the models package
"""
import models.engine.file_storage as file_storage


storage = file_storage.FileStorage()
storage.reload()
