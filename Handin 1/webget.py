import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to="/tmp/"):
    urlParts = url.split('/')
    filename = urlParts[-1]
    #filepath can be set to anything by specifiying the filepath directory
    to = "./"
    filepath = to + filename;
    file = req.urlretrieve(url, filepath)