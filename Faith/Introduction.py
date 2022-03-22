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

constructor.establish_head('Faith',current_page)
print('<header>')
constructor.generate_nav(4)
constructor.generate_header('Faith and Founders','Tales of False Gods')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Chief','Hornet','Axton','Dawn','Dusk','Locket','Prince','Jawson'],0)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('The Five Founders',file.read())
print('</div></main>')

print('</body>')

print('</html>')
