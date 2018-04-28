import RPi.GPIO as GPIO #adds Raspberry pi GPIO library (may need to install this on pi)
import time


CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..','E': '.', 'F': '..-.',
        'G': '--.', 'H': '....','I': '..','J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--','N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-','R': '.-.',
        'S': '...', 'T': '-', 'U': '..-','V': '...-','W': '.--', 'X': '-..-',
        'Y': '-.--','Z': '--..','0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....','6': '-....',  '7': '--...',
        '8': '---..','9': '----.',' ':'/', '.':'.-.-.-', ',':'--..--',':':'---...',
        '?':'..--..', '!':'-.-.--', "'":'.----.','-':'-....-', '/':'-..-.',
        '@': '.--.-.', '=':'-...-', '(':'-.--.', ')':'-.--.-', '+':'.-.-.', ' ':' '}

#Morse Code Rules
#1 dash = 3 dots (1 dot being .2 seconds)
#space between parts of same letter = 1 dot
#space between letters = 3 dots
#space between words = 7 dots

#configure Pi to use the BCM (Broadcom) pin names
GPIO.setmode(GPIO.BCM)

led_pin = 18 #set which pin program will be activating
GPIO.setup(led_pin, GPIO.OUT) #sets led as output or input

try:
    while True:
        sentence = str(input("Enter a word or sentence you would like to translate into morse code:\n"))
        sentence = sentence.upper() # converts input to uppercase
    
        for letter in sentence: #dictionaries can use strings as indicies
            MORSE = str(CODE[letter]) #defines letter definition as variable and string
            for i in range(len(MORSE)): #strings must use integers
                if MORSE[i] == '.':
                    GPIO.output(led_pin, True) #dot
                    time.sleep(0.2)
                    GPIO.output(led_pin, False)
                    time.sleep(0.2)
                elif MORSE[i] == '-':
                    GPIO.output(led_pin, True) #dash
                    time.sleep(0.6)
                    GPIO.output(led_pin, False)
                    time.sleep(0.2)
                elif MORSE[i] == ' ':
                    GPIO.output(led_pin, False) #space between words
                    time.sleep(0.4)
            GPIO.output(led_pin, False) #space between letters
            time.sleep(0.4)
            print("running...")
        

        command = str(input("Press 1 to continue, anything else to quit:\n"))
        if command == '1':
            continue
        else:
            break
finally:
    print("cleaning up")
    GPIO.cleanup()            
            
            
        
        
                
    
    
                   
