from pathlib import Path  # to work with path/files/directories
import shutil  # to copy/move files
from zipfile import ZipFile  # to work with zip files
import csv  # to work with csv files
import json  # to work with json files
import sqlite3  # to work with sqllite
import time  # to work with timestamps
import datetime  # to work with datetime
import random  # to generate random numbers
import webbrowser  # to work with web browsers
from email.mime.multipart import MIMEMultipart  # to send email
from email.mime.text import MIMEText  # to frame text or html body for email
from email.mime.image import MIMEImage  # to attach image to email
import smtplib  # to configure smtp server for email
import sys  # to add command line arguments
import subprocess  # to run other programs

# in windows
Path(r"C:\ProgramFiles\Microsoft")
# in mac or linux
path = Path("/usr/local/bin")

path = Path("package1")
print(path.iterdir())
for p in path.iterdir():
    print(p.name)
print("finding files recursively")
for p in path.rglob("*.py"):
    print(p)

# Zip file
with ZipFile("files.zip", "w") as zip:
    for path in Path("package1").rglob("*.*"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())

path = Path("files.zip")
path.unlink()
