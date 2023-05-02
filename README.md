# GPT-3-Python-Edition
Chat GPT-3 in Python accessed using the API when the main website is down. 

## About
It can write exams, write scripts, give advice, can even teach you how to make a bomb. However, you should
use this with caution! The facts given from the model may be false and information should be taken with a grain of salt.

## Model Engine
#### In-Script Engine swap
By default, it uses text-davinci-003 engine due to its reliablity and good results.
If the user wants to switch engine, than you can change that at the beginning of the script or during the 'ask question' loop.

#### Manual indefinate Engine swap
To forever use an engine of your choice, you can manualy change it in ```main.py``` 
1. comment out lines ```55 - 57``` of ```main.py```.
2. In line ```59```, replace ```engine_input``` with ```"your-engine-here-001"``` 

#### Avalable Engines: 
  -  text-curie-001
  -  text-davinci-003
  -  text-ada-001
  -  text-gpt-3.5-turbo	[WIP]

## Controls 
### Before loop
 - When it asks for engine, input any engine available from Open AI, even if its not listed.
 - To input the API key, you must paste as plain text or it may cause issues. 
### During loop
 - ```Up arrow``` to use previous question inputted. 
 - input ```shutdown``` to kill the script.
 - input ```engine``` to hot-swap the engine.

## Credits
* OpenAI API code by @jacobpowaza 
* Python script by @Pud-of-Mud
* Chat-GPT-3 by Open AI 
