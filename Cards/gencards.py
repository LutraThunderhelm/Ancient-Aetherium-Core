#!/usr/bin/python3

import mysql.connector
import json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

with open('../../../../database-credentials/AncientAetheriumCore.json','r') as file:
	secrets = json.loads(file.read())


##############################
#   WEAPON CARD GENERATION   #
##############################

#Pulling everying in the weapons table from the database to use in the for loop
connection = mysql.connector.connect(
host="AncientAetheriumCore.library.thunderhelm.com",
user=secrets["Username"],
password=secrets["Password"],
database="ancientaetheriumcore"
)

database = connection.cursor()

database.execute("SELECT * FROM Weapons ORDER BY ID;")
weapon_data = database.fetchall()
database.close()

#FONTS!!
title_font = ImageFont.truetype("Card-Resources/Rye.ttf", 40)#Just for name
label_font = ImageFont.truetype("Card-Resources/Rye.ttf", 40)#For single letter labels
speclabel_font = ImageFont.truetype("Card-Resources/Sancreek.ttf", 40)#Labels for specifically the Special Traits
value_font = ImageFont.truetype("Card-Resources/SpecialElite.ttf", 30)#For all values with an attached label
value_spacing = 19 #the value used to keep the value fonts right aligned instead of left
effect_font = ImageFont.truetype("Card-Resources/SpecialElite.ttf", 18)#for just the effect description
font_color = (0, 0, 0)

for x in range(0,len(weapon_data)):
    card_data = weapon_data[x]
    print('Making card {current}/{total} ...'.format(current=str(x+1),total=str(len(weapon_data))))
    print(card_data)

    card = Image.open("Card-Resources/Weapon-Base.png")
    canvas = ImageDraw.Draw(card)


    #----------
    #Name label
    #----------
    canvas.text((25, 20), card_data[2], fill=font_color,font=title_font)
    
    
    #---------------
    #Toughness Label
    #---------------
    toughness_value = str(card_data[14])
    toughness_length = len(toughness_value)

    canvas.text((432, 80), "T", fill=font_color,font=label_font)
    canvas.text((425-(toughness_length*value_spacing), 93), toughness_value, fill=font_color,font=value_font)
    
    
    #-------------
    #Volume Labels
    #-------------

    volume_fields = 0
    volume_spacing = 57
    
    #Barrels Label
    if card_data[13]:
        barrel_value = str(card_data[13])
        barrel_length = len(barrel_value)

        canvas.text((425-(barrel_length*value_spacing), 343), barrel_value, fill=font_color,font=value_font)
    canvas.text((432, 329), "B", fill=font_color,font=label_font)
    volume_fields += 1

    #Pots Label
    if card_data[12]:
        pot_value = str(card_data[12])
        pot_length = len(pot_value)

        canvas.text((425-(pot_length*value_spacing), 343 - (volume_fields * volume_spacing)), pot_value, fill=font_color,font=value_font)
    canvas.text((432, 329 - (volume_fields * volume_spacing)), "P", fill=font_color,font=label_font)        
    volume_fields += 1
    
    #Cans Label
    if card_data[11]:
        can_value = str(card_data[11])
        can_length = len(can_value)

        canvas.text((425-(can_length*value_spacing), 343 - (volume_fields * volume_spacing)), can_value, fill=font_color,font=value_font)
    canvas.text((432, 329 - (volume_fields * volume_spacing)), "C", fill=font_color,font=label_font)    

    #------------
    #Effect Label
    #------------

    effect = "\n".join(textwrap.wrap(card_data[7],23))
    canvas.text((230, 392), effect, fill=font_color,font=effect_font)


    #------------
    #Damage Label
    #------------
    dmg_amount = str(card_data[9])
    dmg_size =  list(card_data[10])[0]
    dmg_value = dmg_amount+"D"+dmg_size
    dmg_length = len(dmg_value)

    canvas.text((104, 597), "DAMG", fill=font_color,font=speclabel_font)
    canvas.text((92-(dmg_length*value_spacing), 614), dmg_value, fill=font_color,font=value_font)

    #-----------
    #Range Label
    #-----------
    range_value = str(card_data[8]) 
    range_length = len(range_value)

    canvas.text((104, 527), "RANG", fill=font_color,font=speclabel_font)
    canvas.text((92-(range_length*value_spacing), 544), range_value, fill=font_color,font=value_font)

    #--------------------
    #Special Traits Logic
    #--------------------
    if card_data[4] == {"RateofFireDiceSize/RateofFireDiceValue"}:
        canvas.text((104, 457), "RoF", fill=font_color,font=speclabel_font)
        canvas.text((92-(len(str(card_data[5]) + "D" + str(card_data[6]))*value_spacing), 474), str(card_data[5]) + "D" + str(card_data[6]), fill=font_color,font=value_font)

    elif card_data[4] == {"RateofDecay"}:
        canvas.text((104, 457), "RoD", fill=font_color,font=speclabel_font)
        canvas.text((92-(len(str(card_data[5]))*value_spacing), 474), str(card_data[5]), fill=font_color,font=value_font)


    elif card_data[4] == {"FUEL/CHRG"}:
        connection = mysql.connector.connect(
        host="AncientAetheriumCore.library.thunderhelm.com",
        user=secrets["Username"],
        password=secrets["Password"],
        database="ancientaetheriumcore"
        )

        database = connection.cursor()

        database.execute("SELECT Name FROM Fuel WHERE ID={};".format(card_data[3]))
        fuel_name = database.fetchall()[0][0]
        database.close()
        
        canvas.text((104, 457), list(card_data[4])[0].split("/")[0], fill=font_color,font=speclabel_font)
        canvas.text((92-(len(str(fuel_name))*value_spacing), 474), str(fuel_name), fill=font_color,font=value_font)

        canvas.text((104, 387), list(card_data[4])[0].split("/")[1], fill=font_color,font=speclabel_font)
        canvas.text((92-(len(str(card_data[6]))*value_spacing), 404), str(card_data[6]), fill=font_color,font=value_font)


    else:
        try:
            canvas.text((104, 457), list(card_data[4])[0].split("/")[0], fill=font_color,font=speclabel_font)
            canvas.text((92-(len(str(card_data[5]))*value_spacing), 474), str(card_data[5]), fill=font_color,font=value_font)

            canvas.text((104, 387), list(card_data[4])[0].split("/")[1], fill=font_color,font=speclabel_font)
            canvas.text((92-(len(str(card_data[5]))*value_spacing), 404), str(card_data[6]), fill=font_color,font=value_font)
        except TypeError:
            pass

    card.save("Weapons/{}.png".format(str(x)))




##############################
#   ATTIRE CARD GENERATION   #
##############################

#Pulling everying in the clothing table from the database to use in the for loop
connection = mysql.connector.connect(
host="AncientAetheriumCore.library.thunderhelm.com",
user=secrets["Username"],
password=secrets["Password"],
database="ancientaetheriumcore"
)

database = connection.cursor()

database.execute("SELECT * FROM Attire ORDER BY ID;")
attire_data = database.fetchall()
database.close()

#FONTS!!
title_font = ImageFont.truetype("Card-Resources/FrederickatheGreat.ttf", 40)#Just for name
subtitle_font = ImageFont.truetype("Card-Resources/FrederickatheGreat.ttf", 25)#Just for location
label_font = ImageFont.truetype("Card-Resources/CabinSketch-Bold.ttf", 45)#For single letter labels
value_font = ImageFont.truetype("Card-Resources/CabinSketch.ttf", 35)#For all values with an attached label
value_spacing = 13 #the value used to keep the value fonts right aligned instead of left
effect_font = ImageFont.truetype("Card-Resources/SyneMono.ttf", 18)#for just the effect description
font_color = (0, 0, 0)

for x in range(0,len(attire_data)):
    card_data = attire_data[x]
    print('Making card {current}/{total} ...'.format(current=str(x+1),total=str(len(attire_data))))
    print(card_data)

    card = Image.open("Card-Resources/Attire-Base.png")
    canvas = ImageDraw.Draw(card)


    #----------
    #Name label
    #----------
    canvas.text((25, 20), card_data[1], fill=font_color,font=title_font)
    

    #--------------
    #Location label
    #--------------
    location_addendum = ''
    if card_data[3] is not None:
        location_addendum = location_addendum + ' - ' + list(card_data[3])[0] + ' Harness'
    elif card_data[2] is not None:
        location_addendum = location_addendum + ' - Armor'
    else:
        location_addendum = location_addendum + ' - Clothing'
    canvas.text((35, 94), list(card_data[4])[0] + location_addendum, fill=font_color,font=subtitle_font)


    #---------------
    #Toughness Label
    #---------------
    if card_data[2] is not None:
        toughness_value = str(card_data[2])
    else:
        toughness_value = '1'
    toughness_length = len(toughness_value)

    canvas.text((437, 80), "T", fill=font_color,font=label_font)
    canvas.text((415-(toughness_length*value_spacing), 87), toughness_value, fill=font_color,font=value_font)


    #-------------
    #Volume Labels
    #-------------

    volume_fields = 0
    volume_spacing = 57
    
    #Barrels Label
    if card_data[8]:
        barrel_value = str(card_data[8])
        barrel_length = len(barrel_value)

        canvas.text((415-(barrel_length*value_spacing), 591), barrel_value, fill=font_color,font=value_font)

    canvas.text((437, 585), "B", fill=font_color,font=label_font)
    volume_fields += 1

    #Pots Label
    if card_data[7]:
        pot_value = str(card_data[7])
        pot_length = len(pot_value)

        canvas.text((415-(pot_length*value_spacing), 591 - (volume_fields * volume_spacing)), pot_value, fill=font_color,font=value_font)
    canvas.text((437, 585 - (volume_fields * volume_spacing)), "P", fill=font_color,font=label_font)        
    volume_fields += 1
    
    #Cans Label
    if card_data[6]:
        can_value = str(card_data[6])
        can_length = len(can_value)

        canvas.text((415-(can_length*value_spacing), 591 - (volume_fields * volume_spacing)), can_value, fill=font_color,font=value_font)
    canvas.text((437, 585 - (volume_fields * volume_spacing)), "C", fill=font_color,font=label_font)   


    #------------
    #Effect Label
    #------------

    effect = "\n".join(textwrap.wrap(card_data[5],33.5))
    canvas.text((30, 475), effect, fill=font_color,font=effect_font) 

    card.save("Attire/{}.png".format(str(x)))



############################
#   KITS CARD GENERATION   #
############################

#Pulling everying in the clothing table from the database to use in the for loop
connection = mysql.connector.connect(
host="AncientAetheriumCore.library.thunderhelm.com",
user=secrets["Username"],
password=secrets["Password"],
database="ancientaetheriumcore"
)

database = connection.cursor()

database.execute("SELECT * FROM Kits ORDER BY ID;")
kits_data = database.fetchall()
database.close()

#FONTS!!
title_font = ImageFont.truetype("Card-Resources/StardosStencil.ttf", 40)#Just for name
subtitle_font = ImageFont.truetype("Card-Resources/StardosStencil.ttf", 35)#Just for location
label_font = ImageFont.truetype("Card-Resources/BlackOpsOne.ttf", 45)#For single letter labels
value_font = ImageFont.truetype("Card-Resources/KellySlab.ttf", 35)#For all values with an attached label
value_spacing = 13 #the value used to keep the value fonts right aligned instead of left
effect_font = ImageFont.truetype("Card-Resources/Delius.ttf", 18)#for just the effect description
font_color = (0, 0, 0)
altfont_color = (255,255,255)

for x in range(0,len(kits_data)):
    
    card_data = kits_data[x]
    print('Making card {current}/{total} ...'.format(current=str(x+1),total=str(len(kits_data))))
    print(card_data)

    card = Image.open("Card-Resources/Kit-Base.png")
    canvas = ImageDraw.Draw(card)


    #----------
    #Name label
    #----------
    canvas.text((25, 17), card_data[1], fill=font_color,font=title_font)
    

    #-----------
    #Class label
    #-----------
    canvas.text((25, 80), list(card_data[2])[0], fill=font_color,font=subtitle_font)


    #---------------
    #Toughness Label
    #---------------
    toughness_value = str(card_data[7])
    toughness_length = len(toughness_value)

    canvas.text((439, 75), "T", fill=altfont_color,font=label_font)
    canvas.text((420-(toughness_length*value_spacing), 83), toughness_value, fill=font_color,font=value_font)


    #-------------
    #Volume Labels
    #-------------

    volume_fields = 0
    volume_spacing = 60
    
    #Barrels Label
    if card_data[6]:
        barrel_value = str(card_data[6])
        barrel_length = len(barrel_value)

        canvas.text((55-(barrel_length*value_spacing), 260), barrel_value, fill=font_color,font=value_font)

    canvas.text((72, 255), "B", fill=altfont_color,font=label_font)
    volume_fields += 1

    #Pots Label
    if card_data[5]:
        pot_value = str(card_data[5])
        pot_length = len(pot_value)

        canvas.text((55-(pot_length*value_spacing), 260 - (volume_fields * volume_spacing)), pot_value, fill=font_color,font=value_font)
    canvas.text((72, 255 - (volume_fields * volume_spacing)), "P", fill=altfont_color,font=label_font)        
    volume_fields += 1
    
    #Cans Label
    if card_data[4]:
        can_value = str(card_data[4])
        can_length = len(can_value)

        canvas.text((55-(can_length*value_spacing), 260 - (volume_fields * volume_spacing)), can_value, fill=font_color,font=value_font)
    canvas.text((72, 255 - (volume_fields * volume_spacing)), "C", fill=altfont_color,font=label_font)   


    #------------
    #Effect Label
    #------------

    effect = "\n".join(textwrap.wrap(card_data[3],43))
    canvas.text((113, 140), effect, fill=font_color,font=effect_font) 

    card.save("Kits/{}.png".format(str(x)))
