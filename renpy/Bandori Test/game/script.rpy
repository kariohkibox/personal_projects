# The script of the game goes in this file.

# Variables for character sprite size when speaking
default speaking_char = None
transform tclose:
    zoom 1.1

transform tdefault:
    zoom 1.0

# Function to handle character sprite zoom when speaking
init python:
    from functools import partial
    def my_zoom(char, event, interact=True, **kwargs):
        if not interact:
            return
        if event == "begin" and char != store.speaking_char:
            if renpy.showing(char):
                renpy.show(char, at_list=[tclose])
                store.speaking_char = char
        elif event == "end":
            if renpy.showing(char):
               renpy.show(char, at_list=[tdefault])


# Declare characters used by this game.
# color: colorizes the name of the character.
# who_outlines: outlines the name label text [stroke size, color, x pos, y pos]
define maya = Character("Maya", color="#99DD88", who_outlines=[ (2, "#333333") ], callback=partial(my_zoom, "maya"))

define yukina = Character("Yukina", color="#881187", who_outlines=[ (2, "#333333") ], callback=partial(my_zoom, "yukina"))
define sayo = Character("Sayo", color="#00AABB", who_outlines=[ (2, "#333333") ], callback=partial(my_zoom, "sayo"))
define lisa = Character("Lisa", color="#DD2200", who_outlines=[ (2, "#333333") ], callback=partial(my_zoom, "lisa"))
define ako = Character("Ako", color="#DD008B", who_outlines=[ (2, "#333333") ], callback=partial(my_zoom, "ako"))
define rinko = Character("Rinko", color="#BBBBBB", who_outlines=[ (2, "#333333") ], callback=partial(my_zoom, "rinko"))

define unkchar = Character("???", color="000000", who_outlines=[ (2, "#333333") ])


# The game starts here.

label start:

    # calls the chapter1 file
    call chapter1

    return
