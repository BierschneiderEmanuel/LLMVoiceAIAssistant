# LLMVoiceAIAssistant
![grafik](https://github.com/BierschneiderEmanuel/LLMVoiceAIAssistant/assets/77926785/aa3587e6-fe28-48aa-ab6e-5043c474283b)

Voice Input Output LLM Ollama OpenHermes Mistral 7B AI Assistant: <br>
Simple but powerful AI Voice assistant using the OpenHermes Mistral 7B model. <br>
Voice input is done by the Google Library for performing speech recognition. <br>
Voice output is realized by the pyttsx3 library. <br>
You can interface the large language model by simply start talking. <br>
The AI assistant output is logged as json into the response_log.txt <br>
The python script interfaces a local Ollama model that runs in a virtualized linux envrionment on a Windows host. <br>
To install the Windows linux virtualization environment and the Ollama model please refer to the following steps: <br>
Win-R <br>
cmd <br>
wsl.exe --install <br>
user newUserName pwd newUserNamePassword <br>
wsl.exe --user root -d ubuntu <br>
apt-get update <br>
apt-get upgrade <br>
curl https://ollama.ai/install.sh | sh <br>
ollama run openhermes <br>

To start the voice assistant run the python script: <br>
Win-R <br>
cmd <br>
python voiceAiAssistant.py <br>
