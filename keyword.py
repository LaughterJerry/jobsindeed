import urllib.request
import re
import json
import webbrowser
import time
import bs4
import nltk

filecheck = json.loads(open("jobslist.json", "r").read())

keywords = {}

is_noun = lambda pos: pos[:2] == 'NN'

def parse(page):
	soup = bs4.BeautifulSoup(page, "html")
	div = soup.find("div", {"id": "jobDescriptionText"})
	return str(div)

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def breakdown(doc):
	tokenized = nltk.word_tokenize(doc)
	nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
	return nouns

viewjob = "https://www.indeed.com/viewjob?cmp={newcmp}&t={newtitle}&jk={jk}&q={newcmp}&vjs=3"

email_jobs = []
curpage = 0
error = 0

for job in filecheck:
	try:
		#view = viewjob.format(**job)
		newcmp = job['cmp'].replace(" ", "+")
		newtitle = job['title'].replace(" ", "+")
		#view = view % (newtitle)

		view = viewjob.format(newcmp=newcmp, newtitle=newtitle, jk=job['jk'])

		page = urllib.request.urlopen(view)
		div = parse(page)
		clean = cleanhtml(div)

		if "python" in clean.lower() or "javascript" in clean.lower():
			email_jobs.append(job)

		words = breakdown(clean)

		sub_words = list(keywords.keys())
		for word in words:
			if word in sub_words:
				keywords[word] += 1
			else:
				keywords[word] = 1
		curpage += 1
		print("success: ", curpage)

	except:
		error+= 1
		print("error: ", error)

thisfile = open("keywords.json", "w")
thisfile.write(json.dumps(keywords))
thisfile.close()

thisfile = open("emailjobs.json", "w")
thisfile.write(json.dumps(email_jobs))
thisfile.close()



