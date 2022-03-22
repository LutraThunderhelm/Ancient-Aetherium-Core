#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Damage'
sub_pages = ['Durability','Mind States','Fatigue']

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Damage Rules',current_page)
print('<header>')
constructor.generate_nav(2)
constructor.generate_header('Damage','Ouch!')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Situational','Navigation','Statuses','Invention','Alchemy','Combat','Damage','Railways-and-Chases'],7)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('Applying Damage',file.read())
constructor.generate_buttons(current_page,sub_pages)

if form.getvalue('subpage') is not None:
	for x in range(0,len(sub_pages)):
		if form.getvalue('subpage') == sub_pages[x]:
			with open(current_page+'-Subpages/'+sub_pages[x]+'.txt','r') as file:
				constructor.generate_article(sub_pages[x],file.read())
			try:
				with open(current_page+'-Subpages/'+sub_pages[x]+'.list','r') as file:
					constructor.generate_article_list(file.read())
			except FileNotFoundError:
				pass
else:
	with open(current_page+'-Subpages/'+sub_pages[0]+'.txt','r') as file:
		constructor.generate_article(sub_pages[0],file.read())
	try:
		with open(current_page+'-Subpages/'+sub_pages[0]+'.list','r') as file:
			constructor.generate_article_list(file.read())
	except FileNotFoundError:
		pass

print('</div></main>')

print('</body>')

print('</html>')
