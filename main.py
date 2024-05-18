# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:37:28 2022
Combat de guerrier aleatoire
@author: Colmanos - LinkoLabs
coded witch spyder python 3.9 in anaconda
Step 1 : Create the players & add the parameter of fight
Step 2 : ceate the boss and add the parameter...
Step 3 : lunch the fight & result the winner
Step 4 : Add the bonus choice ( secret capacity )

     __ _       _     _       ___                    
    / _(_) __ _| |__ | |_    / _ \__ _ _ __ ___   ___
   | |_| |/ _` | '_ \| __|  / /_\/ _` | '_ ` _ \ / _ \
   |  _| | (_| | | | | |_  / /_\\ (_| | | | | | |  __/
   |_| |_|\__, |_| |_|\__| \____/\__,_|_| |_| |_|\___|
          |___/                                      

By LinkoLabs| Colmanos

Entre le nom du joueur : col
Lance le dès secret :
les des sont lancer, vous êtes tombez sur le nombre : 4
Le lancement du des pour l'ia est 4
Bienvenue dans la partie :  col
-----------------------------------------------------------
| Le combattant choisi est :  col de la classe :  Mage   |
| Celui-ci possède :  200 de points de vie                 |
| Celui-ci possède :  15  de points de de atk             |
| Celui-ci possède :  40  de points de defence            |
-----------------------------------------------------------
-----------------------------------------------------------
| Le combattant choisi est :  Bina de la classe :  sage   |
| Celui-ci possède :  200 de points de vie                 |
| Celui-ci possède :  5  de points de de atk             |
| Celui-ci possède :  55  de points de defence            |
-----------------------------------------------------------
Le combat commence entre col et  Bina
            __ _       _     _       _
           / _(_) __ _| |__ | |_    / \
          | |_| |/ _` | '_ \| __|  /  /
          |  _| | (_| | | | | |_  /\_/
          |_| |_|\__, |_| |_|\__| \/  
                 |___/                

le choix du des est sur  4
l'IA avais le nombre : 4
super bonus activé +50 d'attaque pour  col
       __                       _   _
      /__\ ___  _   _ _ __   __| | / |
     / \/// _ \| | | | '_ \ / _` | | |
    / _  \ (_) | |_| | | | | (_| | | |
    \/ \_/\___/ \__,_|_| |_|\__,_| |_|
                                     

--------------------------------------
| Life of :  col  :  200 --|
--------------------------------------
| Life of :  Bina  :  200
--------------------------------------

bonus actif
Les adversaires s'attaque !
il reste 195 point de vie a col  et  135  point de vie a Bina
Il reste donc  135 de vie a : Bina
Il reste donc  195 de vie a : col
       __                       _   ____
      /__\ ___  _   _ _ __   __| | |___ \
     / \/// _ \| | | | '_ \ / _` |   __) |
    / _  \ (_) | |_| | | | | (_| |  / __/
    \/ \_/\___/ \__,_|_| |_|\__,_| |_____|
                                         

--------------------------------------
| Life of :  col  :  195 --|
--------------------------------------
| Life of :  Bina  :  135
--------------------------------------

bonus actif
Les adversaires s'attaque !
il reste 190 point de vie a col  et  70  point de vie a Bina
Il reste donc  70 de vie a : Bina
Il reste donc  190 de vie a : col
       __                       _   _____
      /__\ ___  _   _ _ __   __| | |___ /
     / \/// _ \| | | | '_ \ / _` |   |_ \
    / _  \ (_) | |_| | | | | (_| |  ___) |
    \/ \_/\___/ \__,_|_| |_|\__,_| |____/
                                         

--------------------------------------
| Life of :  col  :  190 --|
--------------------------------------
| Life of :  Bina  :  70
--------------------------------------

bonus actif
Les adversaires s'attaque !
il reste 185 point de vie a col  et  5  point de vie a Bina
Il reste donc  5 de vie a : Bina
Il reste donc  185 de vie a : col
       __                       _   _  _  
      /__\ ___  _   _ _ __   __| | | || |
     / \/// _ \| | | | '_ \ / _` | | || |_
    / _  \ (_) | |_| | | | | (_| | |__   _|
    \/ \_/\___/ \__,_|_| |_|\__,_|    |_|
                                         

--------------------------------------
| Life of :  col  :  185 --|
--------------------------------------
| Life of :  Bina  :  5
--------------------------------------

bonus actif
Les adversaires s'attaque !
il reste 180 point de vie a col  et  -60  point de vie a Bina
   __          _          __    __ _       _     _       _
  /__\ __   __| |   ___  / _|  / _(_) __ _| |__ | |_    / \
 /_\| '_ \ / _` |  / _ \| |_  | |_| |/ _` | '_ \| __|  /  /
//__| | | | (_| | | (_) |  _| |  _| | (_| | | | | |_  /\_/
\__/|_| |_|\__,_|  \___/|_|   |_| |_|\__, |_| |_|\__| \/  
                                     |___/                

col  a gagner !
total des rounds :  5
le choix du des est sur  4
l'IA avais le nombre : 4


"""
from random import shuffle
from pyfiglet import figlet_format

class titre:
    def lancement_des_des():
        des = [1,2,3,4,5]
        global des_choice, des_choix_ia
        shuffle(des)
        des_choix_ia = [1,2,3,4,5]
        shuffle(des_choix_ia)
       
        des_choice = des[0]
        print("les des sont lancer, vous êtes tombez sur le nombre :", des_choice)
       
        print("Le lancement du des pour l'ia est",des_choix_ia[0] )
    def title_game():
        global name_of_hero, des, secret_capacity
        print(figlet_format('   fight Game', font='ogre'))
        print("By BinaryFox | Colmanos")
        global name_of_player
        name_of_player = input("Entre le nom du joueur : ")
        name_of_hero = name_of_player
        print("Lance le dès secret : ")
       
        titre.lancement_des_des()

             
class boss:
         
            def boss_player():
                #global name_of_combattant
                global aleatoire_name_boss, com_atk
                global name_of_combattant
                global life_of_combattant
                aleatoire_name_boss = ["Even","Nova","Link","Bina"]
                aleatoire_life_boss = [50,100,150,200,250,300]
                aleatoire_atk_boss = [5,15,20,25,30,35]
                aleatoire_def_boss = [40,45,50,55,60,56]
                aleatoire_race_boss = ["Mage","sage","tank"]
               
                shuffle(aleatoire_name_boss)
                shuffle(aleatoire_life_boss)
                shuffle(aleatoire_atk_boss)
                shuffle(aleatoire_def_boss)
                shuffle(aleatoire_race_boss)
                print("-----------------------------------------------------------")
                print("| Le combattant choisi est : ",aleatoire_name_boss[0],"de la classe : ", aleatoire_race_boss[0],"  |")
                print("| Celui-ci possède : ",aleatoire_life_boss[0],"de points de vie                 |")
                print("| Celui-ci possède : ",aleatoire_atk_boss[0]," de points de de atk             |")
                print("| Celui-ci possède : ",aleatoire_def_boss[0]," de points de defence            |")
                print("-----------------------------------------------------------")
                life_of_combattant = aleatoire_life_boss[0]
                name_of_combattant = aleatoire_name_boss[0]
                com_atk = aleatoire_atk_boss[0]
               


class personnage:
   #global joueur_atk1
   def accueil_jr(name_of_player):
       global joueur_atk1
       global joueur_life1
       print("Bienvenue dans la partie : ", name_of_player)      
        #Debut de l'initialisation du personnage
       joueur_life = [50,100,150,200,250,300]
       joueur_atk = [10,15,20,25,30,35]
       joueur_def = [40,45,50,55,60,56]
       joueur_race = ["Mage","sage","tank"]
       shuffle(joueur_atk)
       shuffle(joueur_life)
       shuffle(joueur_def)
       shuffle(joueur_race)        
     
       print("-----------------------------------------------------------")
       print("| Le combattant choisi est : ",name_of_player,"de la classe : ", joueur_race[0],"  |")
       print("| Celui-ci possède : ",joueur_life[0],"de points de vie                 |")
       print("| Celui-ci possède : ",joueur_atk[0]," de points de de atk             |")
       print("| Celui-ci possède : ",joueur_def[0]," de points de defence            |")
       print("-----------------------------------------------------------")
       joueur_atk1 = joueur_atk[0]
       joueur_life1 = joueur_life[0]
   
class fight:
    global while_boss_life
    def attaque(joueur, combattant, num_atk, num_life, com_atk, while_boss_life):
        global  vie_hero
        vie_hero = joueur_life1
        while_boss_life = life_of_combattant
        print("Le combat commence entre",joueur, "et ", combattant)
        print(figlet_format('          fight !', font='ogre'))
        num_round = 1
        if des_choice == des_choix_ia[0] :
            print("le choix du des est sur ", des_choice)
            print("l'IA avais le nombre :",des_choix_ia[0])
            print("super bonus activé +50 d'attaque pour ",joueur)
            num_atk = num_atk + 50
        else:
            print("le choix du des est sur ", des_choice)
            print("l'IA avais le nombre :",des_choix_ia[0])
            print("pas de bonus pour", joueur)
           
        while while_boss_life >= 0 or vie_hero >= 0  :
            print(figlet_format('    Round '+str(num_round), font='ogre'))
            print('--------------------------------------')
            print("| Life of : ", joueur, " : ",vie_hero,"--|")
            print('--------------------------------------')
            print("| Life of : ",combattant, " : ",while_boss_life)
            print('--------------------------------------\n')
            num_round += +1
            global winner_hero, loser_boss, loser_hero, winner_boss
            winner_hero = False
            loser_boss = False
            loser_hero = False
            winner_boss = False
           
            if des_choice == des_choix_ia[0] :
                num_atk = joueur_atk1 + 50
                while_boss_life = while_boss_life - num_atk
                vie_hero = vie_hero - com_atk
                print("bonus actif")
            else:
                while_boss_life = while_boss_life - num_atk
                vie_hero = vie_hero - com_atk
           
           
            print("Les adversaires s'attaque !\nil reste", vie_hero ,"point de vie a",joueur," et ", while_boss_life," point de vie a",combattant)
            if vie_hero <= 0 :
                   loser_hero = True
                   winner_boss = True
                   print(figlet_format('End of fight !', font='ogre'))
                   print(joueur, " a perdu  !")
                   print("total des rounds : ", str(num_round))
                   print("le choix du des est sur ", des_choice)
                   print("l'IA avais le nombre :",des_choix_ia[0])
                 
               
                   break
            elif while_boss_life <= 0:
                loser_boss = True
                winner_boss = False
                print(figlet_format('End of fight !', font='ogre'))
                print(joueur, " a gagner !")
                print("total des rounds : ", str(num_round))
                print("le choix du des est sur ", des_choice)
                print("l'IA avais le nombre :",des_choix_ia[0])
             
                break
               
           
            else:
               
                print("Il reste donc ", while_boss_life , "de vie a :",combattant)
                print("Il reste donc ", vie_hero , "de vie a :",joueur)
               
                continue
               
             
           

titre.title_game()
personnage.accueil_jr(name_of_player)
boss.boss_player()

fight.attaque(name_of_player, name_of_combattant, joueur_atk1, joueur_life1,com_atk,life_of_combattant )