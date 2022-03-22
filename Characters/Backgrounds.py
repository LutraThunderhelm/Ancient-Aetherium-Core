#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Backgrounds'
sub_pages = []

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Character Creation',current_page)
print('<header>')
constructor.generate_nav(6)
constructor.generate_header('Character Creation','Start Here')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Social-Ladder','Backgrounds','Skills-and-Traits','Perks','Detriments','Promotion'],2)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('What is a Background anyway?',file.read())

with open(current_page+'.list','r') as file:
	constructor.generate_article_list(file.read())
print('</div></main>')

print('</body>')

print('</html>')
