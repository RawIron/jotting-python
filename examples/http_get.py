from httplib import HTTP

req = HTTP("www.zoo-berlin.de")
req.putrequest("GET", "/?Knut")
req.putheader("Accept", "text/html")
req.putheader("User-Agent", "Python26")
req.endheaders()

ec, em, h = req.getreply()
print ec, em

fd = req.getfile()
textlines = fd.read()
print textlines
fd.close()
