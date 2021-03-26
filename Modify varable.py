# Add your Python code here. E.g.
from microbit import *

hungryness=0

while True:
    if button_a.is_pressed():
        hungryness = hungryness + 1
        display.scroll(hungryness)
    if button_b.is_pressed():
        hungryness = hungryness - 1
        display.scroll(hungryness)
