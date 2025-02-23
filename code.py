import time
from adafruit_magtag.magtag import MagTag
import random

QUOTES = [
    "The more I study, the more insatiable do I feel my genius for it to be. - Ada Lovelace",
    "That brain of mine is something more than merely mortal; as time will show. - Ada Lovelace",
    "Programming is the art of algorithm design and the craft of debugging errant code. - Ellen Ullman",
    "The most damaging phrase in the language is: 'It's always been done that way.' - Grace Hopper",
    "An algorithm must be seen to be believed. - Donald Knuth",
    "Machines take me by surprise with great frequency. - Alan Turing",
    "The computer was born to solve problems that did not exist before. - Bill Gates",
    "The function of good software is to make the complex appear to be simple. - Grady Booch",
    "The best way to predict the future is to invent it. - Alan Kay",
    "A good programmer is someone who always looks both ways before crossing a one-way street. - Doug Linder",
    "The most important property of a program is whether it accomplishes the intention of its user. - C.A.R. Hoare",
    "The purpose of computing is insight, not numbers. - Richard Hamming",
    "The best thing about a boolean is even if you are wrong, you are only off by a bit. - Anonymous",
    "The computer is a moron. - Peter Drucker",
    "The computer is incredibly fast, accurate, and stupid. Man is unbelievably slow, inaccurate, and brilliant. The marriage of the two is a force beyond calculation. - Leo Cherne",
    "The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge. - Stephen Hawking",
    "The real problem is not whether machines think but whether men do. - B.F. Skinner",
    "The question of whether a computer can think is no more interesting than the question of whether a submarine can swim. - Edsger Dijkstra",
    "The computing scientist’s main challenge is not to get confused by the complexities of his own making. - Edsger Dijkstra",
    "The best performance improvement is the transition from the nonworking state to the working state. - John Ousterhout",
    "The trouble with programmers is that you can never tell what a programmer is doing until it’s too late. - Seymour Cray",
    "The best programs are the ones written when the programmer is supposed to be working on something else. - Melinda Varian",
    "The best way to get a project done faster is to start sooner. - Jim Highsmith",
    "The best way to learn is to do. - Paul Halmos",
    "The best way to understand recursion is to begin by understanding recursion. - Anonymous",
    "The best way to predict the future is to create it. - Peter Drucker",
    "The best way to escape from a problem is to solve it. - Alan Saporta",
    "The best way to have a good idea is to have a lot of ideas. - Linus Pauling"
]

magtag = MagTag()

magtag.add_text(
    text_wrap=40,
    text_position=(
        (magtag.graphics.display.width // 2),
        (magtag.graphics.display.height // 2),
    ),
    line_spacing=1,
    text_anchor_point=(0.5, 0.5),  # center the text on x & y
    text_scale=1,
)

quote = random.choice(QUOTES)
magtag.set_text(quote)

# wait 2 seconds for display to complete
time.sleep(2)

# sleep to save battery
magtag.exit_and_deep_sleep(86400)
