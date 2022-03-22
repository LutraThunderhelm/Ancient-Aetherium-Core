#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Perks'
sub_pages = ['Combat','Survival','Social','Academic','Faith']

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
constructor.generate_tabs(['Introduction','Social-Ladder','Backgrounds','Skills-and-Traits','Perks','Detriments','Promotion'],4)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Whats in a Perk',file.read())
constructor.generate_buttons(current_page,sub_pages)

if form.getvalue('subpage') is not None:
	for x in range(0,len(sub_pages)):
		if form.getvalue('subpage') == sub_pages[x]:
			with open(current_page+'-Subpages/'+sub_pages[x]+'.list','r') as file:
				constructor.generate_article_list(file.read())
else:
	with open(current_page+'-Subpages/'+sub_pages[0]+'.list','r') as file:
				constructor.generate_article_list(file.read())

print('</div></main>')

print('</body>')

print('</html>')
