#!/usr/bin/env python
# coding: utf-8



import requests
import json
import gradio as gr


url = "https://experimental.willow.vectara.io/v1/chat/completions"

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": 'You are a Healthcare assistant'
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'customer-id': 'xxxxxxxxxx',
  'x-api-key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}



def add_text(text):
    global payload
    
    payload =  json.loads(payload)
    payload['messages'].append({"role": "user", "content": text})
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    
    system_message = response.json()['choices'][0]['message']
    
    payload =  json.loads(payload)
    payload['messages'].append(system_message)
    
    
    
    chat_transcript = ""
    for message in payload['messages']:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"
    
    payload = json.dumps(payload)

    return chat_transcript


ui = gr.Interface(fn=add_text, inputs="text" , outputs= "text")
ui.launch()







