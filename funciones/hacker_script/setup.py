from distutils.core import setup
import py2exe
import os
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import re
import glob

setup(console=["hackerscript.py"])
