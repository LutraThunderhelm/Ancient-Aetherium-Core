#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Royalty'

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("/home/dh_6fequb/library.thunderhelm.com/public/Ancient-Aetherium-Core"))
import constructor

constructor.establish_head('Tales | Occupations',current_page)
print('<header>')
constructor.generate_nav(2)
constructor.generate_header('Occupations','Jobs and More')
print('</header>')

print('<body>')
constructor.generate_tab_directory(os.getcwd())
constructor.generate_tabs(['Royalty','Nobility','Guilds','Military','Workers','Ruins'],-1)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('What is an Occupation',file.read())

print('</div></main>')

print('</body>')

print('</html>')
