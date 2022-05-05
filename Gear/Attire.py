#!/usr/bin/python3

import mysql.connector
import cgi, cgitb, json
cgitb.enable() 

form = cgi.FieldStorage()
current_page = 'Attire'
sub_pages = ['Clothing','Harness','Armor']

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Attire',current_page)
print('<header>')
constructor.generate_nav(3)
constructor.generate_header('Attire','Stay Fashionable')
print('</header>')

print('<body>')
constructor.generate_tabs(['Introduction','Brawling-Weapons','Firing-Weapons','Attire','Kits','Husks'],3)

print('<main><div id=content>')
with open(current_page+'.txt','r') as file:
	constructor.generate_article('How to wear Attire',file.read())
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

database.execute("SELECT * FROM Attire ORDER BY Artifact;")
attire_data = database.fetchall()
database.close()

print('<div id="Card-Holder">')
for x in range(0,len(attire_data)):
    if attire_data[x][2] is not None and "Armor" == current_subpage:
        print('<div class="Attire-Card">')
        print('<img src="/Ancient-Aetherium-Core/Cards/Attire/' + str(attire_data[x][0]-1)+ '.png">')
        print('<span>'+str(attire_data[x][9])+' $A</span>')
        print('</div>')
    elif attire_data[x][3] is not None and "Harness" == current_subpage:
        print('<div class="Attire-Card">')
        print('<img src="/Ancient-Aetherium-Core/Cards/Attire/' + str(attire_data[x][0]-1)+ '.png">')
        print('<span>'+str(attire_data[x][9])+' $A</span>')
        print('</div>')
    elif attire_data[x][2] is None and attire_data[x][3] is None and "Clothing" == current_subpage:
        print('<div class="Attire-Card">')
        print('<img src="/Ancient-Aetherium-Core/Cards/Attire/' + str(attire_data[x][0]-1)+ '.png">')
        print('<span>'+str(attire_data[x][9])+' $A</span>')
        print('</div>')

print('</div>')
    
print('</div></main>')

print('</body>')

print('</html>')
