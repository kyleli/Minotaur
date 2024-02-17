# Minotaur

Minotaur is a command-line interface (CLI) tool designed to simplify various tasks such as audio recording, transcription, and summarization. It is primarily focused on generating summaries of meetings based on transcripts using GPT (Generative Pre-trained Transformer) models.

## Dependencies
Minotaur has minimal dependencies:
- Python
- OpenAI API
- pyaudio
- keyboard
- pyaudio

## Setup
1. Clone the Minotaur repository from GitHub.
2. Install Python and the required dependencies.
3. Replace the `API_KEY` parameter in `config.py` with your OpenAI API key or set up an environmental variable for your API key on your operating system.

## Usage
To use Minotaur, follow these steps:

1. **Recording Audio**: If you want to enable custom audio recording, set the `ENABLE_AUDIO_RECORDING` flag to `True`. You can also enable the `ENABLE_WHISPER` flag to transcribe audio. Ensure that the debug transcript and audio files are set to `False`.
   
2. **Transcription**: Minotaur uses Whisper for audio transcription. Enable Whisper by setting the `ENABLE_WHISPER` flag to `True`. If using custom audio, specify the path to the audio file.

3. **Summarization**: Minotaur utilizes GPT models for summarization. Ensure that `ENABLE_GPT` is set to `True`. You can customize the summarization process by modifying the `SYSTEM_PROMPT` and `SUMMARY_COMMAND_PATH` variables.

4. **Running Minotaur**: Execute `main.py` to start Minotaur. It will guide you through the process of audio recording, transcription, and summarization. Follow the prompts to finalize the summary or customize the summarization process based on the transcript.

## Configuration
- `CONVERSATION_TYPE`: Type of conversation (e.g., "A meeting").
- `LANGUAGE`: Language of the conversation (e.g., "English").
- `WHISPER_MODEL_ID`: Whisper model identifier.
- `AUDIO_PATH`: Path to the audio file.
- `MODEL_ID`: GPT model identifier.
- `TEMPERATURE`: Temperature value for generating responses.
- `PRESENCE_PENALTY`: Presence penalty value for generating responses.
- `MAX_TOKENS`: Maximum number of tokens allowed for the conversation.
- `TRANSCRIPT_PATH`: Path to the transcript file.
- `SYSTEM_PROMPT`: Instructions for the summarization tool.
- `SUMMARY_COMMAND_PATH`: Path to the file containing summarization commands.
- `API_KEY`: OpenAI API key.
- `ENABLE_AUDIO_RECORDING`: Flag to enable custom audio recording.
- `ENABLE_WHISPER`: Flag to enable Whisper transcription.
- `ENABLE_GPT`: Flag to enable GPT summarization.
- `ENABLE_DEBUG_TRANSCRIPT`: Flag for using a debug transcript file.
- `DEBUG_TRANSCRIPT_PATH`: Path to the debug transcript file.
- `ENABLE_DEBUG_AUDIO`: Flag for using a debug audio file.
- `DEBUG_AUDIO_PATH`: Path to the debug audio file.
