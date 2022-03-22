#!/usr/bin/python3

import mysql.connector
import cgi, cgitb, json
cgitb.enable() 

form = cgi.FieldStorage()
current_page = 'Brawling-Weapons'
sub_pages = ['Powered','Breaker','Blades','Gauntlet','Thrown']

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Brawling Weapons',current_page)
print('<header>')
constructor.generate_nav(3)
constructor.generate_header('Brawling Weapons','Up Close and Personal')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Brawling-Weapons','Firing-Weapons','Attire','Kits','Husks'],1)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('What is a Brawling Weapon?',file.read())
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

with open('../../../../database-credentials/AncientAetheriumCore.json','r') as file:
	secrets = json.loads(file.read())

connection = mysql.connector.connect(
host="AncientAetheriumCore.library.thunderhelm.com",
user=secrets["Username"],
password=secrets["Password"],
database="ancientaetheriumcore"
)

database = connection.cursor()

database.execute("SELECT * FROM Weapons ORDER BY Artifact;")
weapon_data = database.fetchall()
database.close()

print('<div id="Card-Holder">')
for x in range(0,len(weapon_data)):
    if list(weapon_data[x][1])[0] == current_subpage:
        print('<div class="Weapon-Card">')
        print('<img src="/Ancient-Aetherium-Core/Cards/Weapons/' + str(weapon_data[x][0]-1)+ '.png">')
        print('<span>'+str(weapon_data[x][15])+' $A</span>')
        print('</div>')
print('</div>')
    
print('</div></main>')

print('</body>')

print('</html>')
