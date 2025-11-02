from google import genai
from google.genai import types
import wave

#os.environ["GOOGLE_API_KEY"] = "your-gemini-api-key"

client = genai.Client()

file_path = input("Enter your file absolute path: ")
target_language = input("Enter your language the document should be summarised in: ")

# Upload the PDF using the File API
sample_file = client.files.upload(
  file=file_path,
)
complete_prompt = f''' Summarise the document in {target_language} '''

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_file, complete_prompt])
translated_content = response.text
print(response.text)

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)


response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents=translated_content,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data
file_name='audio_clip.wav'
wave_file(file_name, data) # Saves the file to current directory
print("Translated audio summary is successfully saved in current directory")
