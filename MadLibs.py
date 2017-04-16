import time

print ("Let's play Mad Libs!")

hero = input ("Please give a noun: ")
heroName = input ("Please enter a name:")
heroAdj1 = input ("Enter an adjective: ")
weapon = input ("Enter a noun")
storyPlace = input ("Enter the name of a place:")
minions = input ("Enter a plural noun:")
questVerb1 = input ("Enter a verb: ")
questMinion1 = input ("Enter a plural noun: ")
questVerb2 = input ("Enter a verb: ")
questMinion2 = input ("Enter a plural: ")
questVerb3 = input ("Enter a verb: ")
questPlace = input ("Enter the name of another place:")
questVerb4 = input ("Enter a verb: ")
number = input ("Enter a number: ")
questItem = input ("Enter a plural noun: ")
bossAdj = input ("Enter an adjective: ")
bossNoun = input ("Enter a noun: ")
bossVerb = input ("Enter a verb: ")
pastPlace = input ("Enter the name of another place: ")
heroVerb1 = input ("Enter a verb: ")
heroAdj2 = input ("Enter an adjective: ")
heroNoun1 = input ("Enter a noun: ")
heroNoun2 = input ("Enter a noun: ")
heroVerb2 = input ("Enter a verb ending with -ing:")
heroNoun3 = input ("Enter a noun: ")
heroPlace = input ("Enter a place: ")
battleAdj1 = input ("Enter an adjective: ")
battleAdj2 = input ("Enter an adjective: ")
heroVerb3 = input ("Enter a verb in past tense: ")
endPlace = input ("Enter a place: ")
endAdj = input ("Enter an adjective: ")
endNoun = input ("Enter a noun: ")
end = ("Final one! Enter an adverb: ")

print("Now Loading your epic story!")
time.sleep(10)

print ("Once upon a time there was a " + hero + " named " + heroName+ ". They were very"  + heroAdj1 + " as their weapon was a " + weapon + ". In all of" + storyPlace + ", nobody else had such a weapon. That is why when the  " + questMinion1 + "came,"
+ heroName + " was chosen without a doubt. Using their " + weapon + ", they were sent to" + questVerb1 + "the" + questMinion1 +
       " .In order to do this, they had to " + questVerb2 + " the " + questMinion2 + "," + questVerb3 + " all the way to "  + questPlace +
       ", and " + questVerb4 + " " + number + " " + questItem + ".Finally, once all has been done, they have to face the "
        +  bossAdj + " " + bossNoun + " .This " + bossNoun + " was "  + bossAdj +  " as it had been known to " + bossVerb + pastPlace
        + ". However, " + heroName + " believed that he/she could " + heroVerb1 + " it. After all, he/she was known as the "
        + heroAdj1 +" "  + heroNoun1 + ", the " + heroNoun2 + " of "  + heroVerb2 + " and " + " the " + heroNoun3 + " from "
         + heroPlace + ". After a "  + battleAdj1 + "and "  + battleAdj2 + "battle, he/she " + heroVerb3 +"  it.  As a reward, the people of"
         + endPlace + " gave him/her a " + endAdj + " " + endNoun + " and they lived " + endAdj + " ever after.")

#if noun starts with a vowel, change a to an

#if  noun.startswith('a' or 'e'or 'i'or  'o' or 'u'):
    #'a/an' = 'an'
    #else
    #'a/an' = 'a'
