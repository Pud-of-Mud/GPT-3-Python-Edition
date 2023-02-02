#Open AI's ChatGPT-3 within Python using Open AI's Open API.
#Can write exams, write scripts, give advice, can
#even teach you how to make a bomb. However, you should
#use this with caution! The facts given from the 
#model may be false and should be taken with a grain of salt.

import os
import openai
from colorama import Fore, Style
import pwinput
from time import sleep

#Defining Varables
apiKeyVarable = os.environ['api-key']
thePhrase = os.environ['phrase']

#Defining what to do when a question is asked
#using the openai APT.
def askquestion(question, engine):
  completion = openai.Completion.create(
    engine=model_engine,
    prompt=question,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )
  response = completion.choices[0].text
  print(response + '\n')

#Opening statements to get the API key, 
#than leads into main loop.
if __name__ == "__main__":
  
  #Giving credit where credit is due
  print(Fore.GREEN + 'Open AI Code by @jacobpowaza \n' + Style.RESET_ALL)
  print(Fore.GREEN + 'Made by @Pud0fMud \n' + Style.RESET_ALL)
  sleep(0.5)

  find = "You can find your api key at: "  
  for char in find:
    sleep(0.08)
    print(char, end='', flush=True)

  sleep(0.7)
  print(Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)
  sleep(0.7)

  apiKeyWords = "\nPlease input your API key:"
  
  for char in apiKeyWords:
    sleep(0.08)
    print(char, end='', flush=True)
    
  
  key = pwinput.pwinput(prompt='\n', mask='*')
  secretPhraseAcc = "Secert Phrase Accepted!\nLoading API...\n"

  #Applying the user's API key if given proper 
  #one; unless using secret phrase ;)
  if (key == thePhrase):
    openai.api_key = apiKeyVarable
    for char in secretPhraseAcc:
      sleep(0.05)
      print(char, end='', flush=True)
    
    sleep(1)
  else:
    openai.api_key = key

  #Uses text-davinci-003 engine due to its reliablity and good results.
  #If user wants to switch engine, than you can change that here.
  #Avalable Engines: 
  #  -  text-curie-001
  #  -  text-ada-001
  #Replace the string in the model_engine varable to change.

  model_engine = "text-davinci-003"
    
  engine = "GPT-3 is using the " + Fore.GREEN + "text-davinci-003" + Style.RESET_ALL + " engine.\n\n"
  for char in engine:
    sleep(0.07)
    print(char, end='', flush=True)

  #Question loop. Asks question, than uses
  #function askquestion() as defined at the top.
  while True:
    question = None
    question = input('Enter Question: ')
    if question:
      askquestion(question, model_engine)