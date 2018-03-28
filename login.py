# -*- coding: utf-8 -*-
# Lib HelloWorld Forked!
import LINETOKEN
from LINETOKEN.lib.Gen.ttypes import *
from datetime import datetime
from Helper.main import qr
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess
import urllib

botStart = time.time() 

token = LINETOKEN.LINE()
token.login(token=qr().get())
token.loginResult()

print "\n\nGet Token Success!"
reload(sys)
sys.setdefaultencoding('utf-8')

sys.exit('Thx For Using this bot Token!')

def bot(op):
	pass
while True:
	bot(token.stream())
