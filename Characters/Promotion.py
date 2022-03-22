#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Promotion'
sub_pages = []

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Promotion',current_page)
print('<header>')
constructor.generate_nav(6)
constructor.generate_header('Promotion','Power Increased')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Social-Ladder','Backgrounds','Skills-and-Traits','Perks','Detriments','Promotion'],6)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Handling a Promotion',file.read())

print('</div></main>')

print('</body>')

print('</html>')
