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

constructor.establish_head('Character Creation',current_page)
print('<header>')
constructor.generate_nav(6)
constructor.generate_header('Character Creation','Start Here')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Social-Ladder','Backgrounds','Skills-and-Traits','Perks','Detriments','Promotion'],0)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Characters',file.read())

with open('Intro-Bears.txt','r') as file:
	constructor.generate_article('What is a Bear',file.read())

with open('Intro-Char-Creation.txt','r') as file:
	constructor.generate_article('Time to build a bear!',file.read())    

print('</div></main>')

print('</body>')

print('</html>')
