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

constructor.establish_head('Rules',current_page)
print('<header>')
constructor.generate_nav(2)
constructor.generate_header('Introduction to AA Rules','Listen to the Ruin Master')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Situational','Navigation','Statuses','Invention','Alchemy','Combat','Damage','Railways-and-Chases'],0)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Rules and You',file.read())
print('</div></main>')

print('</body>')

print('</html>')
