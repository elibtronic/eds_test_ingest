#EDS Ingest Tester#

tim@elibtronic.ca
-I'll answer as best I can-

This script was created to check how long it takes for a catalogue MARC record to be ingested and added to the EDS local index.

##Instructions

1. Download and install [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) This provides the base screen scraping functionality needed
2. Adjust BASE_URL to reflect how you get to EDS and your accession record id
3. Fill in the 'bib' array with unique identifiers required to access an item directly into EDS
4. It will check if the item is already in EDS site and then check every 15 minutes until found

All results are logged.

Eg.

[http://proxy.library.brocku.ca/login?url=http://search.ebscohost.com/login.aspx?direct=true&db=cat00778a&AN=bu.b2378491&site=eds-live&scope=site](http://proxy.library.brocku.ca/login?url=http://search.ebscohost.com/login.aspx?direct=true&db=cat00778a&AN=bu.b2378491&site=eds-live&scope=site)
is a direct link to item

unique id is
bu.b2378491

Some quick experimentation should reveal your necessary syntax
