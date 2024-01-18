""" Copyright 2024 Emanuel Bierschneider

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. """
import speech_recognition as sr
import pyttsx3
from base64 import b64decode
from pathlib import Path
from io import BytesIO
from urllib.parse import urlencode
import subprocess
import json
import jsonstreams

def generate_stream_json_response(prompt):
    data = json.dumps({"model": "openhermes", "prompt": prompt})
    process = subprocess.Popen(["curl", "-X", "POST", "-d", data, "http://localhost:11434/api/generate"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    full_response = ""
    with jsonstreams.Stream(jsonstreams.Type.array, filename='./response_log.txt') as output:
        while True:
            line, _ = process.communicate()
            if not line:
                break
            try:
                record = line.decode("utf-8").split("\n")
                for i in range(len(record)-1):
                    data = json.loads(record[i].replace('\0', ''))
                    if "response" in data:
                        full_response += data["response"]
                        with output.subobject() as output_e:
                            output_e.write('response', data["response"])
                    else:
                        return full_response.replace('\n', "").replace('\0', '')
                if len(record)==1:
                    data = json.loads(record[0].replace('\0', ''))
                    if "error" in data:
                        full_response += data["error"]
                        with output.subobject() as output_e:
                            output_e.write('error', data["error"])
                return full_response.replace('\n', "").replace('\0', '')
            except Exception as error:
                # handle the exception
                print("An exception occurred:", error)
    return full_response.replace('\n', "").replace('\0', '')

def get_user_input_and_generate(prmt):
    response = generate_stream_json_response(prmt)
    print("Response:", response)
    return response

if __name__ == '__main__':   
    # Init text 2 speech
    engine = pyttsx3.init()
    # Listen for audio input
    while True:
        # Init speech recognizer
        r = sr.Recognizer()
        # Wait for audio input
        with sr.Microphone() as source:
            print("Speak now:")
            audio = r.listen(source)
        # Recognize the audio
        try:
            response_text = ""
            prompt = r.recognize_google(audio, language="en-EN", show_all=False)
            print("You asked:", prompt)
            # Generate AI response
            response_text = get_user_input_and_generate(prompt)
            # Speak the response
            engine.say(response_text)
            engine.runAndWait()
        # Catch if error
        except Exception as error:
            # handle the exception
            #print("An exception occurred:", error)
            engine.runAndWait()
