#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Statuses'
sub_pages = []

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Status Rules',current_page)
print('<header>')
constructor.generate_nav(2)
constructor.generate_header('Status Rules','How They Effect You')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Situational','Navigation','Statuses','Invention','Alchemy','Combat','Damage','Railways-and-Chases'],3)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('When to use statuses',file.read())

with open(current_page+'.list','r') as file:
	constructor.generate_article_list(file.read())
print('</div></main>')

print('</body>')

print('</html>')
