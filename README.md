# GPT-3-Python-Edition
## About
<img align="right" width="200" src="https://user-images.githubusercontent.com/109466200/235973666-7eb55030-bb1e-4edc-b40f-7befba441790.png">
ChatGPT within Python, being accessed through the API when the main website is down or at max capacity.
<br>
<br>
ChatGPT is an AI chatbot that uses natural language processing to create humanlike conversational dialogue. The language model can respond to questions and compose various written content, including articles, social media posts, essays, code and emails. 
<a href="https://en.wikipedia.org/wiki/ChatGPT"><i>Source</i><a>

 ## Depreciation of this project 
This project will likely never be finished due to the recent change of policy with OpenAI.
Access to the API is now restricted to paying users for their service. Be aware of this before using this project!
<br> <br>
However, if you'd like to finish the project or add to it your free to make as many commits to it as you please. 
I am no longer spending time on this project as of now.


## Limitations
You should use this with caution! 
The facts given from the language model may be false and information should be taken with a grain of salt. 
<br>
The model also has no memory of past conversations ATM. 

## Model Engine
#### In-Script Engine swap
By default, it uses text-davinci-003 engine due to its reliablity and good results.
If the user wants to switch engine, than you can change that in two ways: 
 - at the beginning of the script 
 - during the 'ask question' loop.

#### Manual fixed Engine swap
To forever use an engine of your choice, you can manualy change it in ```main.py``` 
1. comment out most of the following code of ```main.py```

```python
  # Sets the engine to be used. Can be switched out in runtime.  
  # Defaults to text-davinci-003
  print('\nPlease pick your text generation engine. \n\nAvailable Engines: \n * text-davinci-003 [Best results] \n * text-curie-001 [Fastest, ok results]\n * text-ada-001 [Cheap to run]\n\nIf left blank, it will default to text-davinci-003\n\n')

  engine_input = input('Input: ')

  if engine_input == "":
    engine_input = "text-davinci-003"
  
  model_engine = engine_input
```

2. In the final line of the former code, replace ```engine_input``` with ```"your-engine-here-001"``` 

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

## Deployment

1. Download the latest stable release [here](https://github.com/Pud-of-Mud/GPT-3-Python-Edition/releases/tag/v0.1.1) or beta release [here](https://github.com/Pud-of-Mud/GPT-3-Python-Edition) 
2. To run the application, run ```main.py``` in any python compiler or IDE.
3. You will need a OpenAI account and an API key to run the script.
   
## Licence 
This project is protected under the [GNU Affero General Public License v3.0](/LICENSE)

## Credits
* OpenAI API code by @jacobpowaza 
* Python script by @Pud-of-Mud
* Chat-GPT by OpenAI
