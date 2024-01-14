# LLMVoiceAIAssistant
Voice Input Output LLM Ollama OpenHermes Mistral 7B AI Assistant
Simple but powerful AI Voice assistant using the OpenHermes Mistral 7B model.
Voice input is done by the Google Library for performing speech recognition.
Voice output is realized by the pyttsx3 library.
You can interface the large language model by simply start talking.
The ai assistant output is logged as json into the response_log.txt.
The python script interfaces a local Ollama model running in a virtualized linux envrionment on a Windows host.
To install the Windows linux virtualization environment and the Ollama model please refer to the following steps:
Ctrl-X
wsl.exe --install
user newUserName pwd newUserNamePassword
wsl.exe --user root -d ubuntu
apt-get update
apt-get upgrade
curl https://ollama.ai/install.sh | sh
ollama run openhermes

To start the voice assistant run the python script:
Ctrl-X
python voiceAiAssistant.py
