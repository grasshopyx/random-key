#!/usr/local/bin/python3
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m","--mode",help="give the modes, e.g., major and minor")
parser.add_argument("-k","--key", help="give the keys, e.g., C and D")
parser.add_argument("-s","--scaletype", help="give the scale types, e.g., harmonic and melodic")
parser.add_argument("-t","--traditional", help="natural major, harmonic minor and melodic minor", action="store_true")
#  The option is now more of a flag than something that requires a value. We even changed the name of the option to match that idea. Note that we now specify a new keyword, action, and give it the value "store_true". This means that, if the option is specified, assign the value True to args.verbose. Not specifying it implies False.

args = parser.parse_args()


# keys = ( "C", "Db", "D","Eb","E","F","Gb","G","Ab","A","Bb","B",
#          "c", "c#", "d","eb","e","f","f#","g","g#","a","bb","b")
keys = ("C", 
        "D-flat/C-sharp", 
        "D",
        "E-flat",
        "E",
        "F",
        "G-flat/F-sharp",
        "G",
        "A-flat/G-sharp",
        "A",
        "B-flat",
        "B",
        )

scale_types = ("natural",
         "harmonic",
         "melodic",
        )

modes = ("major/Ionian",
        "Dorian",
        "Phrygian",
        "Lydian",
        "Mixolydian",
        "minor/Aeolian",
        "Locrian",
        )



key = random.choice(keys)


if args.traditional : # with action="store_true", it is always not None
    modes = modes[0:1] + modes[5:6] # or ( modes[0], modes[5] )

mode = random.choice(modes)

if args.traditional :
    if mode == modes[0] : # major
        scale_types = scale_types[0:1]
    elif mode == modes[1] : # minor
        scale_types = scale_types[1:3]

scale_type = random.choice(scale_types)


print(key+' '+scale_type+' '+mode)
