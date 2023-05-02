#Dependinces 
import os
import openai
from colorama import Fore, Style
import pwinput
from time import sleep

#Defining Varables
apiKeyVarable = os.environ['api-key']
thePhrase = os.environ['phrase']
#TextEngines
textDavinci = 'text-davinci-003'
textCurie = 'text-curie-001' 
textAda = 'text-ada-001'

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
  
  # Uncomment the following line when working with developmental 
  # branches; however re-comment before merging to main. 
  #print(Fore.RED + 'Developer Build!\n' + Style.RESET_ALL)
  print(Fore.RED + "WARNING: All engines cannot recall from memory ATM.\n"  + Style.RESET_ALL)

  # API key is kept in memory and never stored locally. 
  # TODO: allow the user to save API key.
  find = "You can find your api key at: "  
  for char in find:
    sleep(0.04)
    print(char, end='', flush=True)
  
  sleep(0.7)
  print(Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)
  sleep(0.7)

  apiKeyWords = "\nPlease input your API key:"  
  for char in apiKeyWords:
    sleep(0.04)
    print(char, end='', flush=True)
  
  key = pwinput.pwinput(prompt='\n', mask='*')
  openai.api_key = key
  
  # Sets the engine to be used. Can be switched out in runtime.  
  # Defaults to text-davinci-003
  print('\nPlease pick your text generation engine. \n\nAvailable Engines: \n * text-davinci-003 [Best results] \n * text-curie-001 [Fastest, ok results]\n * text-ada-001 [Cheap to run]\n\nIf left blank, it will default to text-davinci-003\n\n')

  engine_input = input('Input: ')

  if engine_input == "":
    engine_input = "text-davinci-003"
  
  model_engine = engine_input
  engine = "\nGPT-3 is using the " + Fore.GREEN + model_engine + Style.RESET_ALL + " engine.\n\n"
  for char in engine:
    sleep(0.03)
    print(char, end='', flush=True)

  # Explains to the user how it works and its limitations
  sleep(0.5)
  print("Controls: \n Up arrow key to insert previous question.\n Type 'shutdown' to kill the script.\n type 'engine' to hot-swap language model.\n")
  
  
  # Question loop. Asks question, than uses function
  # askquestion() as defined at the top.
  while True:
    question = None
    question = input('Enter Question: ')
    if question == 'shutdown':
      break
    elif question == 'engine':
      engine_input = input("Please input the desired engine: ")
      model_engine = engine_input
    else:
      askquestion(question, model_engine)