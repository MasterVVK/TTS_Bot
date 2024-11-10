from elevenlabs import save
from elevenlabs.client import ElevenLabs
import config
import uuid  # Импортируем модуль для генерации случайных имен файлов

client = ElevenLabs(
    api_key=config.elevenlabs_api_key,
)

def get_all_voices():
    voices = client.voices.get_all()
    return [{'name': voice.name, 'id': voice.voice_id} for voice in voices.voices]

def generate_audio(text: str, voice: str):
    audio = client.generate(
        text=text,
        voice=voice,
        model="eleven_multilingual_v2"
    )
    # Генерация случайного имени файла
    unique_filename = f"Audio/{uuid.uuid4().hex}.mp3"
    save(audio, unique_filename)
    return unique_filename
