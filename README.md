# smolagents_1
Today, we will create an agent with the smolagents library using a mistral-small:24b model.

---
you need : 

- ollama : https://ollama.com
- mistral-small:24b : ollama pull mistral-small:24b

---
1) create an virtual environment : "python3 -m venv venv" after when the environment is create "source venv/bin/activate"
<img width="692" height="86" alt="Capture d’écran 2025-11-05 à 16 57 23" src="https://github.com/user-attachments/assets/1a0cee99-7a71-47c7-8037-d8026d95a2f6" />
<img width="700" height="62" alt="Capture d’écran 2025-11-05 à 16 58 07" src="https://github.com/user-attachments/assets/21723b0c-2b48-4f98-ab26-eea0d8dd1526" />

2) install smolagents'library : "pip install smolagents litellm duckduckgo-search ollama"
<img width="634" height="63" alt="Capture d’écran 2025-11-05 à 16 58 39" src="https://github.com/user-attachments/assets/ab0a23d1-d703-4749-ba2f-d8bd252cc563" />

3) in the file model1.py ou put the code if you do not downoald the file.
<img width="879" height="243" alt="Capture d’écran 2025-11-05 à 17 03 42" src="https://github.com/user-attachments/assets/93dddf18-3218-47dc-a904-ddaf014c6e42" />

4) in our terminal we need to do two things :
   - ollama serve
   - ollama run mistral-small:24b
<img width="620" height="207" alt="Capture d’écran 2025-11-05 à 17 14 02" src="https://github.com/user-attachments/assets/eb736a89-73f7-4865-90ee-24ee10afbec5" />
<img width="633" height="219" alt="Capture d’écran 2025-11-05 à 17 14 22" src="https://github.com/user-attachments/assets/17e20a6f-9757-4e73-bc2b-669107fa96bc" />


6) run the code 
<img width="850" height="165" alt="Capture d’écran 2025-11-05 à 16 59 23" src="https://github.com/user-attachments/assets/2c299817-c18e-4d21-b63c-e0611a9c47a4" />

---
# explain the code : 

in first we need to now the begining of the code is that : 

<img width="543" height="24" alt="Capture d’écran 2025-11-05 à 17 06 08" src="https://github.com/user-attachments/assets/98bd4c54-d55f-4275-bba5-27022f5551c1" />

this are the dependencies of our agent. we call the DuckDuckgo for the web research, liteLLMModel for our mistral-small:24b and the principale library/dependencies is smolagents.

in the second part of the code we have : 
  - model = LiteLLMModel(model_id="ollama_chat/mistral-small:24b", api_base="http://127.0.0.1:11434", num_ctx=8192)
  - agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
this two line are the most important because this line are calling our model ai and choice the tokens'limit.

--- 
# Which AI model for smolagents ?

The more parameters the model has, the better it will be. to my point of view mistral's model are the best 

<img width="1493" height="875" alt="Capture d’écran 2025-11-05 à 17 19 55" src="https://github.com/user-attachments/assets/13e92309-a7fc-4b57-b125-e3efba201e42" />

i think if your model have more than 12b parameter it's good


