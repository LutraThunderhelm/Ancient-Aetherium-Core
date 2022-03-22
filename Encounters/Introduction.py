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

constructor.establish_head('Encounters | Introduction',current_page)
print('<header>')
constructor.generate_nav(0)
constructor.generate_header('Encounters and Enemies','Combat at the ready')
print('</header>')

print('<body>')
print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Under Construction',file.read())
print('</div></main>')

print('</body>')

print('</html>')
