import os

# Whisper Config
CONVERSATION_TYPE = "A meeting"
LANGUAGE = "English"
WHISPER_MODEL_ID = 'whisper-1'
AUDIO_PATH = 'output.mp3'

# GPT Config
IS_LOCAL = False # CHANGE THIS TO TRUE FOR LOCAL, FALSE FOR OPENAI
MODEL_ID = 'gpt-3.5-turbo'
TEMPERATURE = 0.2
PRESENCE_PENALTY = -0.1
MAX_TOKENS = 4096 # DEPRECATED THAT
TRANSCRIPT_PATH = 'transcript.txt'
SYSTEM_PROMPT = """
You are a summarization tool designed to summarize meeting minutes.
- You will be given a transcript and a series of summarization commands, templates, and changes to make.
- Your goal is to summarize the meeting into a minutes report that is formatted according to the template provided.
- You will only create the minutes and not write anything else. If you need more information or can not give a factual answer, write "N/A".
- Do not add additional content or fields that are not specified in the template you are provided.
"""

# Summary Config
SUMMARY_COMMAND_PATH = 'debug_examples/summary_command.txt'

# API Key
API_KEY = os.environ.get('OPENAI_API_KEY') # Change me to your OpenAI API key

# DEBUGGING MODULES
ENABLE_AUDIO_RECORDING = False # Fallback to sample recording
ENABLE_WHISPER = False # Fallback to sample transcript
ENABLE_GPT = True

# DEBUGGING EXAMPLE FILES
ENABLE_DEBUG_TRANSCRIPT = True
DEBUG_TRANSCRIPT_PATH = 'debug_examples/meeting_transcript.txt'
ENABLE_DEBUG_AUDIO = True
DEBUG_AUDIO_PATH = 'debug_examples/meeting_sample.mp3'