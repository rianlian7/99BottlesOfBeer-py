'''
Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

#RULES

1. If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
2. Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
3. Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4. Put a blank line between each verse of the song.'''

''' 99 bottles of beer on the wall, 99 bottles of beer.
    Take one down and pass it around, 98 '''
'''1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.'''

x = 99

while (x != 0):
    y = str(x)
    o = x - 1
    z = str(o)
    bot = " bottles"
    if ( x == 1):
       bot = " bottle"
       z = "no more"
    print(y + bot + " of beer on the wall, " + y + bot + " of beer.")
    print("Take one down and pass it around, " + z + " bottles of beer on the wall.\n")
    x -= 1
    
x = 99
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, "+ str(x) + " bottles of beer on the wall.\n")