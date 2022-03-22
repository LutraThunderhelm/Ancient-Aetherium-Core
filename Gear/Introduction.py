#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Introduction'
sub_pages = []

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Gear',current_page)
print('<header>')
constructor.generate_nav(3)
constructor.generate_header('Gear and Equipment','Your One Stop Shop')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Brawling-Weapons','Firing-Weapons','Attire','Kits','Husks'],0)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Artifacts, Pots, and How to Use Them',file.read())
with open('Intro-to-Cards.txt','r') as file:
	constructor.generate_article('Item Handling',file.read())
print('</div></main>')

print('</body>')

print('</html>')
