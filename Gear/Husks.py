#!/usr/bin/python3

import mysql.connector
import cgi, cgitb, json
cgitb.enable() 

form = cgi.FieldStorage()
current_page = 'Husks'
sub_pages = ['Limbs','Senses','Casting']

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Husks',current_page)
print('<header>')
constructor.generate_nav(3)
constructor.generate_header('Husks','Mind and Body')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Brawling-Weapons','Firing-Weapons','Attire','Kits','Husks'],5)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Husks and Mind Channels',file.read())
constructor.generate_buttons(current_page,sub_pages)

if form.getvalue('subpage') is not None:
    current_subpage = form.getvalue('subpage')
else:
    current_subpage = sub_pages[0]

for x in range(0,len(sub_pages)):
	if current_subpage == sub_pages[x]:
		with open(current_page+'-Subpages/'+sub_pages[x]+'.txt','r') as file:
			constructor.generate_article(sub_pages[x],file.read())
		try:
			with open(current_page+'-Subpages/'+sub_pages[x]+'.list','r') as file:
				constructor.generate_article_list(file.read())
		except FileNotFoundError:
			pass

print('</div>')
    
print('</div></main>')

print('</body>')

print('</html>')
