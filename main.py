import os
import openai
from colorama import Fore, Style
import pwinput
from time import sleep

#Defining Varables
apiKeyVarable = os.environ['api-key']
thePhrase = os.environ['phrase']

#Defining what to do when a question is asked
#using OpenAI's API.
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
  print(Fore.GREEN + 'Open AI API Code by @jacobpowaza ' + Style.RESET_ALL)
  print(Fore.GREEN + 'Made by @Pud0fMud \n' + Style.RESET_ALL)
  sleep(0.5)
  print(Fore.RED + 'Developer Build!\n' + Style.RESET_ALL)

  find = "You can find your api key at: "  
  for char in find:
    sleep(0.07)
    print(char, end='', flush=True)

  sleep(0.7)
  print(Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)
  sleep(0.7)

  apiKeyWords = "\nPlease input your API key:"
  
  for char in apiKeyWords:
    sleep(0.08)
    print(char, end='', flush=True)
    
  
  key = pwinput.pwinput(prompt='\n', mask='*')
  openai.api_key = key

  #Sets the engine to be used. Can be switched out in runtime.  
  words = 'Pick your engine: \nAvailable Engines: \n * text-davinci-003 [Best results] \n * text-curie-001 [Fastest, ok results]\n * text-ada-001 [unknown]\nIf left empty, it will default to davinci-003\n\n '

  for char in words:
    sleep(0.04)
    print(char, end='', flush=True)

  engine_input = input('Input: ')
  
  model_engine = engine_input
  engine = "\nGPT-3 is using the " + Fore.GREEN + model_engine + Style.RESET_ALL + " engine.\n\n"
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