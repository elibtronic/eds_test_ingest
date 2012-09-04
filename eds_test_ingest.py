# EDS Ingest Tester
#
# Fill in the bib array with the unique identify used to create your EDS records
# Change BASE_URL to reflect your EDS setup and Catalogue Accession Number
# After uploading your .MARC to to your Ebsco FTP start this script
# 

from bs4 import BeautifulSoup
import urllib,httplib,datetime,time,sys

logname = "log_" + str(time.time()) + ".txt"
BASE_URL = "http://proxy.library.brocku.ca/login?url=http://search.ebscohost.com/login.aspx?direct=true&db=cat00778a&AN=bu."

bib = [
    'b2378495',
    'b2378491',
    'b2378487',
    'b2378486',
    'b2378485'
    ]

urls = []

def construct_url(b):
    return BASE_URL+b+"&site=eds-live&scope=site"

def log_start():
    f = open(logname,"a")
    f.write("Started checking at: " + str(datetime.datetime.now())+ "\n")
    f.close()

def log_no(url):
    f = open(logname,"a")
    f.write("Found: " + url + " at " + str(datetime.datetime.now())+ "\n")
    f.close()

def first_check(urls_list):
    print "Seeing if bibs are already in EDS"
    for u in urls_list:
        s = BeautifulSoup(urllib.urlopen(u).read())
        if (s.find_all(text='No results were found.')):
            pass
        else:
            print "...found an item already in EDS: ",u
            sys.exit()
    print "... Items are unique"


#start up
log_start()
f = open(logname,"a")
f.write("Bibs that will be checked\n")
for b in bib:
    urls.append(construct_url(b))
    f.write(construct_url(b)+"\n")
f.close()
first_check(urls)

while True:
    print "Checking another round"
    for u in urls:
        s = BeautifulSoup(urllib.urlopen(u).read())
        if (s.find_all(text='No results were found.')):
            pass
        else:
            log_no(u)
            print "found an item!"
            sys.exit()
    print "...done\n"
    time.sleep(900)
