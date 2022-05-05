#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
current_page = 'Arcane-Star'

print("Content-type: text/html\n\n")
print("<html>")

import sys, os
sys.path.append(os.path.abspath("../"))
import constructor

constructor.establish_head('Arcane Star','Arcane-Star')
print('<header>')
constructor.generate_nav(5)

print('<div id="banner">')

import json
with open('Foundations/star.json','r') as file:
    star = json.loads(file.read())
    star = star['star']

print('<form action="Arcane-Star">')
print('<section id="Arcane-Star">')

for y in range(0,9):
    print('<div class="Star-Row">')
    for x in range(0,13):
        if star[y][x] == "":
            print('<div class="Star-Item"><img src="Foundations/Icons/Place-Holder.svg"></div>')
        else:
            print('<div class="Star-Item"><button type="submit" name="foundation" class="Foundation-Container" value={name}><img src="Foundations/Icons/{name}.svg" class="Foundation-Icon"><br><span class="Spell-Names">{name_clean}</span></button></div>'.format(name=star[y][x],name_clean=star[y][x].replace("-"," ")))
    print('</div>')

print('</section>')
print('</form>')
print('</div>')
print('</header>')
print('<body>')
print('<main>')
if form.getvalue('foundation') is not None:
    with open('Foundations/Descriptions/{foundation}.json'.format(foundation=form.getvalue('foundation')), 'r') as foundation_file:
        foundation = json.loads(foundation_file.read())
    print('<h2><span>'+form.getvalue('foundation').replace('-',' ')+'</span></h2>')
    print(foundation['description'])

    print('<table id=Spell-List>')
    for x in range(0,int(len(foundation['spells'])/4)):
        print('<tr>')
        for y in range(0,4):
            print('<td>')
            current_spell = foundation['spells'][(y*int(len(foundation['spells'])/4)) + x]
            print('<h3><span>{name}</span></h3><br>'.format(name=current_spell['name']))
            print('<h4 id="Spell-Stats">Arcane Points: ' + current_spell['ap'] + '<br>')
            print('Arcane Bank: ' + current_spell['ab'] + '<br>')
            print('Casting Time: ' + current_spell['castingTime'] + '</h4><br>')
            print(current_spell['description'])
            print('</td>')
        print('</tr>')
    print('</table>')
else:
    with open(current_page + '.txt','r') as file:
	    constructor.generate_article('What is Arcana?',file.read())
print('</main>')
print('</body>')
print('</html>')
