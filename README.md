# Voice-Controlled Desktop Assistant using Python

A Python-based voice assistant that recognizes spoken commands and performs basic desktop tasks such as opening websites, fetching information, and speaking responses.

---

## Features

- Voice command recognition
- Open websites (Google, YouTube, StackOverflow)
- Wikipedia search and summary
- Speak responses using text-to-speech
- Open WhatsApp Web, Microsoft Edge, and Opera GX
- Search on Google, YouTube, StackOverflow, Wikipedia, Edge, and Opera GX
- Tell current time

---

## Demo

The assistant recognizing and executing a voice command:

![Jarvis Demo](demo.png)

---

## Example Commands
- open youtube
- search python tutorial on youtube
- open google
- search cricket score on google
- open stack overflow
- search react hooks on stack overflow
- open wikipedia
- wikipedia taj mahal
- open whatsapp
- open edge
- edge search latest news
- open opera gx
- opera gx search gaming laptop

## Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- Wikipedia API

---

## How to Run

1. Clone the repository
   git clone https://github.com/Parinay-Chauhan/jarvis-voice-assistant

2. Install dependencies
   pip install -r requirements.txt

3. Run the assistant
   python main.py

  
---

## How It Works

The assistant listens to microphone input using the SpeechRecognition library.  
The captured speech is converted into text and matched with predefined commands.

Based on the recognized command, the assistant performs actions such as:

- Opening websites via webbrowser
- Fetching summaries using Wikipedia API
- Speaking responses using pyttsx3

The system runs continuously to allow real-time voice interaction.

---

## Future Improvements

- Wake-word detection ("Hey Jarvis")
- AI conversational capabilities
- Desktop automation commands
- Graphical user interface (GUI)
- Cross-platform support

---

## Author

Parinay Chauhan  
BCA Student | Aspiring Software Developer  
 
   

   
