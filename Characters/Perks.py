#!/usr/bin/python3

import mysql.connector
import json
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Perks'
sub_pages = ['Any','Arcane','Creationist','Martial','Mastermind','Follower','Tailor','Socialite','Shade']
levels = ['Any','1','5','10','20','30','50']

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

backgrounds = []
level = 'Any'

if form.getvalue('background1') != None:
	backgrounds.append(form.getvalue('background1'))
else:
	backgrounds.append('Any')
if form.getvalue('background2') != None:
	backgrounds.append(form.getvalue('background2'))
else:
	backgrounds.append('Any')

if form.getvalue('level'):
	level = form.getvalue('level')

print('<form id=Perk-Query>')
print('<div id="Background-Selector"><h3>Backgrounds: </h3>')
for x in range(1,3):
	if x == 2:
		print(" and ")
	print('<select name="background'+str(x)+'">')
	print('<option value="'+backgrounds[x-1]+'">'+backgrounds[x-1]+'</option>')
	for y in range(0,len(sub_pages)):
		print('<option value="'+sub_pages[y]+'">'+sub_pages[y]+'</option>')
	print('</select>')
print('</div>')

print('<div id="Level-Selector"><h3>Level: </h3>')
print('<select name="level">')
print('<option value="'+level+'">'+level+'</option>')
for x in range(0,len(levels)):
	print('<option value="'+levels[x]+'">'+levels[x]+'</option>')
print('</select></div>')

print('<input type="submit" id="Perk-Query-Submit" name="Search" value="Search"></form>')


if backgrounds[0] == backgrounds[1]:
	backgrounds.pop(1)
	backgrounds.append('Any')
	backgrounds.append(backgrounds[0])
	backgrounds.pop(0)
elif sub_pages.index(backgrounds[0]) > sub_pages.index(backgrounds[1]):
	backgrounds.append(backgrounds[0])
	backgrounds.pop(0)



with open('../../../../database-credentials/AncientAetheriumCore.json','r') as file:
	secrets = json.loads(file.read())

connection = mysql.connector.connect(
host="AncientAetheriumCore.library.thunderhelm.com",
user=secrets["Username"],
password=secrets["Password"],
database="ancientaetheriumcore"
)

database = connection.cursor()

level_addendum = ''

if level != 'Any':
	level_addendum = 'level="'+str(level)+'"'

if backgrounds[0] == 'Any':
	if backgrounds[1] == 'Any':
		if level_addendum != '':
			database.execute('SELECT * FROM Perks WHERE '+level_addendum+' ORDER BY ID;')
		else:
			database.execute('SELECT * FROM Perks ORDER BY ID;')
	else:
		if level_addendum != '':
			database.execute('SELECT * FROM Perks WHERE FIND_IN_SET("'+backgrounds[1]+'",Backgrounds)>0 AND '+level_addendum+' ORDER BY ID')
		else:
			database.execute('SELECT * FROM Perks WHERE FIND_IN_SET("'+backgrounds[1]+'",Backgrounds)>0 ORDER BY ID')
else:
	if level_addendum != '':
		database.execute('SELECT * FROM Perks WHERE FIND_IN_SET("'+backgrounds[1]+'",Backgrounds)>0 AND FIND_IN_SET("'+backgrounds[0]+'",Backgrounds)>0 AND '+level_addendum+' ORDER BY ID')
	else:
		database.execute('SELECT * FROM Perks WHERE FIND_IN_SET("'+backgrounds[1]+'",Backgrounds)>0 AND FIND_IN_SET("'+backgrounds[0]+'",Backgrounds)>0 ORDER BY ID')

perk_data = database.fetchall()
database.close()

perk_string = ''

for x in range(0,len(perk_data)):
    current_perk = perk_data[x]
    perk_string += current_perk[1] + '\n'
    if current_perk[5] != '':
        perk_string += current_perk[5] + '\n'
    else:
        perk_string += '/Ancient-Aetherium-Core/placeholder.png\n'
    perk_string += 'Backgrounds: ' + list(current_perk[3])[0] + ', ' + list(current_perk[3])[1] + '\n'
    perk_string += 'Level: ' + list(current_perk[2])[0] + '\n'
    perk_string += current_perk[4]
    if x != len(perk_data)-1:
        perk_string += '\n\n'

constructor.generate_article_list(perk_string)

print('</div></main>')

print('</body>')

print('</html>')
