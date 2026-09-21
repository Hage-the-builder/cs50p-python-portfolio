import sys
import random
from pyfiglet import Figlet
                                    #importing packages


figlet = Figlet()
figlet.getFonts()
figlet.getFonts()
fonts = figlet.getFonts()
                                    #getting font list and difining terms



if len(sys.argv) == 1:
        font_name = random.choice(fonts)   #if not font is stateed pick a rondom one


elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font_name = sys.argv[2]
    if font_name not in fonts:
        sys.exit("ERRRRRORRRRRR")
                                        #makes the font stated into a font and checks if its in the list if not ERRRRRRORRROOROROR

else:
        sys.exit("ERRRRORORROROROR")
                                             #if nothing is stated the program or has too many terms says ERRRRRRORRROOROROR


pretext = input("Input: ")
                                    #asks for text berfore fontification
figlet.setFont(font=font_name)
                                #sets the font
print(figlet.renderText(pretext))
                                        #makes text fontified :)
