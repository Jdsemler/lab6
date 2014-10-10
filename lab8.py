# Partner lab 8 example

import random



playerHealth = 100
monsterHealth = 100
firepunchDmg = 5
blazekickDmg = 10
fireballDmg = 30

# TODO:
# Loop - When should it stop?
# Input - user gets to choose attack
# Calculating the damage done by the user and the monster
# Output - printing damage
# Printing a victory message

print "A Wild Pikachu Appears! Prepare To fight!"

print "Blaziken! I Choose You!"
print "*Blaziken has 100 health, Pikachu Has 100 Health"

b = True

while(b):
    print "Which Attack Will Blaziken Use?"
    print "-----------------------------------------------"
    print "    ATTACKS: firepunch blazekick fireball"
    print "-----------------------------------------------"
    playerinput = raw_input ()
    if playerinput == "firepunch":
        monsterHealth = monsterHealth - firepunchDmg
    if playerinput == "blazekick":
        monsterHealth = monsterHealth - blazekickDmg
    if playerinput == "fireball":
        monsterHealth = monsterHealth - fireballDmg
        
    damageBymonster = random.randint (1,35)
    playerHealth = playerHealth - damageBymonster
    print "the monster has damaged you by"
    print str(damageBymonster)
    print "The monsters health is: " + str(monsterHealth)
    
    print "The players health is: " + str(playerHealth)
    
    if monsterHealth <= 0:
        print "The Wild Pikachu Has Fainted"
        b = False
    if playerHealth <= 0:
        print "Blaziken Has Fainted, You Run To The Nearest Pokemon Center"
        b = False
#if raw_input = punchDmg then monsterHealth - punchDmg