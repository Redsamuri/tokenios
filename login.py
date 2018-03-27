# -*- coding: utf-8 -*-
# Lib HelloWorld Forked!
import LINETOKEN
from LINETOKEN.lib.Gen.ttypes import *
from datetime import datetime
from Helper.main import qr
from time import sleep
from bs4 import BeautifulSoup
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz
import wikipedia, urllib
from gtts import gTTS
from googletrans import Translator

botStart = time.time() 

cl = LINETOKEN.LINE()
cl.login(token=qr().get())
cl.loginResult()

print "\n\nGet Token Success!"
reload(sys)
sys.setdefaultencoding('utf-8')

while True:
	bot(cl.stream())
