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

constructor.establish_head('Welcome',current_page)
print('<header>')
constructor.generate_nav(7)
constructor.generate_header('The Ancient Aetherium','Magic and Mystery')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction'],0)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Welcome to the Ancient Aetherium',file.read())
print('</div></main>')

print('</body>')

print('</html>')
