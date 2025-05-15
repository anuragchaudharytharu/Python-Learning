# 2. Install external module and run it
import pyttsx3

twinkle = """Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are."""
print(twinkle)

engine = pyttsx3.init()
engine.say(twinkle)
engine.runAndWait()