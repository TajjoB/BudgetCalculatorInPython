# This is Budget Calculator in python

import pyttsx3 # Output speech
import speech_recognition as sr # Input speech
from word2number import w2n # Changes numbers as words to numbers as floats for calculations

# initialize engine
engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 170)     # setting up new voice rate

def speak(output):
  engine.say(output)
  engine.runAndWait()



########################
speak("How much is your net Income per annum?")


record = sr.Recognizer()

with sr.Microphone() as source:

    print("Listening...")
    incomeAnswer = record.listen(source,timeout=2)
    

try:
    print("Thinking...")
    incomeGoogle = record.recognize_google(incomeAnswer, language = 'en-in')
    incomeGoogle = incomeGoogle.lower()
    incomeGoogle = w2n.word_to_num(incomeGoogle)
    print(incomeGoogle)

except sr.UnknownValueError(): 
    print("Error 0 with speech recognition")
    quit()
 

speak("Do you [own], [mortgage] or [rent] your house?")


record = sr.Recognizer()

with sr.Microphone() as source:

    print("Listening...")
    livingAnswer = record.listen(source,timeout=2)
    

try:
    print("Thinking...")
    livingGoogle = record.recognize_google(livingAnswer, language = 'en-in')
    livingGoogle = livingGoogle.lower()
    print(livingGoogle)

except sr.UnknownValueError(): 
    print("Error 1 with speech recognition")
    quit()


carValue = (incomeGoogle/3)
carValue = round(carValue)

# Rent
rentUtility = incomeGoogle * 0.0333 / 12
rentUtility = round(rentUtility)
rentFood = incomeGoogle * 0.0333 / 12
rentFood = round(rentFood)
rentUpkeep = incomeGoogle * 0.0333 / 12
rentUpkeep = round(rentUpkeep)
rentAmount = (incomeGoogle * 0.333) / 12
rentAmount = round(rentAmount)
rentSave = (incomeGoogle * 0.233) / 12
rentSave = round(rentSave)

# Mortgage

mortgageUtility = incomeGoogle * 0.0333 / 12
mortgageUtility = round(mortgageUtility)
mortgageFood = incomeGoogle * 0.0333 / 12
mortgageFood = round(mortgageFood)
mortgageUpkeep = incomeGoogle * 0.0333 / 12
mortgageUpkeep = round(mortgageUpkeep)
mortgageAmount = (incomeGoogle * 0.333) / 12
mortgageAmount = round(mortgageAmount)
mortgageSave = (incomeGoogle * 0.233) / 12
mortgageSave = round(mortgageSave)

# Own
# playMoney = houseValue/16
ownUtility = incomeGoogle * 0.0333 / 12
ownUtility = round(ownUtility)
ownFood = incomeGoogle * 0.0333 / 12
ownFood = round(ownFood)
ownUpkeep = incomeGoogle * 0.0333 / 12
ownUpkeep = round(ownUpkeep)
ownSave = (incomeGoogle * 0.56) / 12
ownSave = round(ownSave)



if livingGoogle == "rent":
  speak(f"Spend no more than {carValue} dollars on your car! Ensure utilities don't exceed {rentUtility} dollars per month! Spend {rentFood} dollars per month on food. Spend {rentUpkeep} dollars per month on toiletries. Ensure your rent does not exceed {rentAmount} dollars per month! You will save at least {rentSave} dollars per month.")

elif livingGoogle == "mortgage":
  speak(f"Spend no more than {carValue} dollars on your car! Ensure utilities don't exceed {mortgageUtility} dollars per month! Spend {mortgageFood} dollars per month on food. Spend {mortgageUpkeep} dollars per month on toiletries. Ensure your rent does not exceed {mortgageAmount} dollars per month! You will save at least {mortgageSave} dollars per month.")

elif livingGoogle == "own":
  speak("What is the current value of your house?")

  record = sr.Recognizer()

  with sr.Microphone() as source:


      print("Listening...")
      livingAnswer = record.listen(source,timeout=2)
      

  try:
      print("Thinking...")
      livingGoogle = record.recognize_google(livingAnswer, language = 'en-in')
      livingGoogle = livingGoogle.lower()
      livingGoogle = w2n.word_to_num(livingGoogle)
      print(livingGoogle)

  except sr.UnknownValueError(): 
      print("Error 1 with speech recognition")
      quit()
  
  playMoney = livingGoogle/16

  speak(f"Spend no more than {carValue} dollars on your car! Ensure utilities don't exceed {ownUtility} dollars per month! Spend {ownFood} dollars per month on food. Spend {ownUpkeep} dollars per month on toiletries. You will save at least {ownSave} dollars per month. You can buy cash, if you can afford to, and maintain a luxury such as a sports car or boat if it doesnt exceed {playMoney} dollars")

else:
  speak("Living situation not stated correctly! Program ended! Restart program and state 'rent', 'mortgage' or 'own'!")


speak("This was Budget Calculator in Python. Goodbye.")

quit()
######################################################################