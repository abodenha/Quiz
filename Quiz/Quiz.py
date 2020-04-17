import RPi.GPIO as GPIO    
from time import sleep     
GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)   
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)    
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

questions = [{"question":["What is 159-47?","1: 113", "2: 112", "3: 145"], "answer": 2}, 
             {"question":["Bobby has 36 toy cars. He gives 19 of them to his mom. How many toy cars does Bobby have left?", "1: 17 toy cars", "2: 55 toy cars", "3: 19 toy cars"], "answer": 1},  
             {"question":["What is 6x60?", "1: 36", "2: 420", "3: 360"], "answer": 3}, 
             {"question":["How many days are in April?", "1: 30", "2: 31", "3: 28"], "answer": 1}, 
             {"question":["How many milliliters are in a liter?", "1: 1000ml", "2: 1000000ml", "3: 100ml"], "answer": 1}]

while True:
  for question in questions: 
    for line in question["question"]:
      print (line)


    print("Which answer do you choose 1, 2, or 3?")
    while GPIO.input(21) != GPIO.HIGH:
      answer = 0
    answer = 1  

    if int(answer) == question["answer"]:
      print ("Correct")
      GPIO.output(12, GPIO.HIGH) # Turn on
      sleep(1)                  # Sleep for 1 second
      GPIO.output(12, GPIO.LOW)  # Turn off
    else:
      print ("Incorrect")
      GPIO.output(24, GPIO.HIGH) # Turn on
      sleep(1)                  # Sleep for 1 second
      GPIO.output(24, GPIO.LOW)  # Turn off