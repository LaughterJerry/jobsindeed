import urllib.request
import re
import json
import webbrowser

curpage = 0
jobs = []

for curpage in range(100):
	if curpage < 1:
		page = urllib.request.urlopen('https://www.indeed.com/jobs?q=programmer&l=remote')
	else:
		page = urllib.request.urlopen('https://www.indeed.com/jobs?q=programmer&l=remote&start=' + str(curpage*10))

	print(curpage)

	pagetext = str(page.read())

	jobs1 = pagetext.split("var jobmap = {};", 1)[1].split("</script>", 1)[0].split("\\n")

	jobs2 = []

	viewjob = "https://www.indeed.com/viewjob?cmp={cmp}&t={title}&jk={jk}&q={cmp}&vjs=3"

	for job in jobs1:
		if job != "":
			jobr = job.split("]= ", 1)[1]
			jobr = jobr.replace("'", '"')
			jobr = jobr.replace("\\", "")
			jobr = jobr.replace('jk:', '"jk":')
			jobr = jobr.replace('efccid:', '"efccid":')
			jobr = jobr.replace('srcid:', '"srcid":')
			jobr = jobr.replace('cmpid:', '"cmpid":')
			jobr = jobr.replace('num:', '"num":')
			jobr = jobr.replace('srcname:', '"srcname":')
			jobr = jobr.replace('cmp:', '"cmp":')
			jobr = jobr.replace('cmpesc:', '"cmpesc":')
			jobr = jobr.replace('cmplnk:', '"cmplnk":')
			jobr = jobr.replace('loc:', '"loc":')
			jobr = jobr.replace('country:', '"country":')
			jobr = jobr.replace('zip:', '"zip":')
			jobr = jobr.replace('city:', '"city":')
			jobr = jobr.replace('title:', '"title":')
			jobr = jobr.replace('locid:', '"locid":')
			jobr = jobr.replace('rd:', '"rd":')
			jobr = jobr.rstrip(";")
			jobs2.append(jobr)

	for job in jobs2:
		try:
			jobs.append(json.loads(job))
		except:
			pass

	#for job in jobs:
	#	#webbrowser.open(viewjob.format(**job))
	#	for line in job.keys():
	#		print(line, "\t", job[line])

print(len(jobs))

#thisfile = open("jobslist.json", "w")
#thisfile.write(json.dumps(jobs))
#thisfile.close()


