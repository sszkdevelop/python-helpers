from flask import Blueprint, render_template, request, url_for, redirect

from textminer import TextMiner

from textmanager import *
from QueryAPI import *

import string
import time
import threading
import re

from werkzeug.utils import secure_filename

import os

import datefinder

UPLOAD_PAGE = Blueprint("upload_page", __name__)
upload_dir = "static/Users/harsha/"


def isvalidfile(name):
    if name.endswith(".doc"):
        return True
    elif name.endswith(".docx"):
        return True
    elif name.endswith(".pdf"):
        return True
    return False


def isdoc(name):
    if name.endswith(".doc"):
        return True
    return False


def isdocx(name):
    if name.endswith("docx"):
        return True
    return False


def ispdf(name):
    if name.endswith(".pdf"):
        return True
    return False


def doctotxt(doc):
    miner = TextMiner()
    filetext = miner.read_document(doc)
    return filetext

@UPLOAD_PAGE.route("/upload", methods=["GET", "POST"])
def upload():
    """
    routes to upload page
    """
    error = None

    message = ""

    if request.method == "POST":
        uploaded_files = request.files.getlist("file[]")
        numfiles = len(uploaded_files)

        for file in uploaded_files:
            filename = secure_filename(file.filename)
            if isvalidfile(filename):
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)
                file.save(os.path.join(upload_dir, filename))

                filetext = doctotext(upload_dir + filename)
                # print filetext

                # dates = datefinder.find_dates(filetext, source=True)
                # for date in dates:
                #     # print dir(date)
                #     print date[1]

                resdata = getdata(filetext)
                resdata["name"] = filename
                resdata["path"] = upload_dir + filename

                if isdoc(filename):
                    nfn = filename.replace(".doc", ".txt")
                    ntxtfile = open(upload_dir + nfn, "w")
                    ntxtfile.write(filetext)
                    ntxtfile.close()
                elif isdocx(filename):
                    nfn = filename.replace(".docx", ".txt")
                    ntxtfile = open(upload_dir + nfn, "w")
                    ntxtfile.write(filetext)
                    ntxtfile.close()

            else:
                print "Not accepted filetype: " + filename

    return render_template("upload.html", message=message, error=error)
