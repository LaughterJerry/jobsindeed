import urllib.request
import re
import json
import webbrowser
import time
import bs4
import nltk

jobfile = json.loads(open("emailjobs.json", "r").read())

viewjob = "https://www.indeed.com/viewjob?cmp={newcmp}&t={newtitle}&jk={jk}&q={newcmp}&vjs=3"

for job in jobfile:
	newcmp = job['cmp'].replace(" ", "+")
	newtitle = job['title'].replace(" ", "+")
	view = viewjob.format(newcmp=newcmp, newtitle=newtitle, jk=job['jk'])
	webbrowser.open(view)

	input("next...")

