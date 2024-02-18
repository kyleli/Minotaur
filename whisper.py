from openai import OpenAI
from config import CONVERSATION_TYPE, LANGUAGE, WHISPER_MODEL_ID

client = OpenAI()

def convert_audio(media_file_path, TRANSCRIPT_PATH):
    """
    Converts audio file to text using OpenAI's Whisper API and stores the transcript in a text file.

    Args:
    - api_key (str): The API key for accessing the OpenAI API.
    - media_file_path (str): The path to the audio file.
    """
    with open(media_file_path, 'rb') as media_file:
        response = client.audio.transcriptions.create(
            model=WHISPER_MODEL_ID,
            file=media_file,
            prompt=f"This is a conversation about {CONVERSATION_TYPE} in {LANGUAGE}.",
            response_format='text'
        )
        with open(TRANSCRIPT_PATH, 'w', encoding='utf-8') as transcript_file:
            transcript_file.write(response)
        
if __name__ == '__main__':
    convert_audio('debug_examples/real_meeting_sample.mp3', 'transcript.txt')