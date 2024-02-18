import record
import whisper
import gpt
import fileprocessing
from config import *

def main():
    HandleAudioRecording()
    HandleWhisperTranscription()
    HandleGPTSummarization()

def HandleAudioRecording():
    if ENABLE_AUDIO_RECORDING:
        record.record_audio(AUDIO_PATH)
    else:
        print("Audio Recording Disabled")

def HandleWhisperTranscription():
    if ENABLE_WHISPER:
        if ENABLE_DEBUG_AUDIO:
            whisper.convert_audio(API_KEY, DEBUG_AUDIO_PATH, TRANSCRIPT_PATH)
        else:
            whisper.convert_audio(API_KEY, AUDIO_PATH, TRANSCRIPT_PATH)
    else:
        print("Whisper Disabled")

def HandleGPTSummarization():
    summary = ""
    modification_commands = ""
    accepted = False

    while not accepted:
        conversation_log = []
        
        if ENABLE_GPT:
            if ENABLE_DEBUG_TRANSCRIPT:
                conversation_log = gpt.initialize_system_prompt(SYSTEM_PROMPT, DEBUG_TRANSCRIPT_PATH)
            else:
                conversation_log = gpt.initialize_system_prompt(SYSTEM_PROMPT, TRANSCRIPT_PATH)

            print("Processing Summary")
            summarization_command = fileprocessing.read_from_file(SUMMARY_COMMAND_PATH)
            summary = gpt.process_summarization_query(MODEL_ID, TEMPERATURE, PRESENCE_PENALTY, conversation_log, summarization_command, summary, modification_commands)
            print(summary)
            print("Completed Processing")

            # Ask the user if they want to stop generating summaries
            user_input = input("Finalize this summmary? (y/n): ")
            if user_input.lower() == 'y':
                accepted = True
                fileprocessing.write_output_to_file(summary, 'summary.txt')
                print("Saved Summary to debug_examples/summary.txt")
            else:
                # Currently hardcoded, need the generation algo here.
                q1 = input("Make the meeting tone seem: \n1. Neutral\n2. Aggressive\n3. Positive\n4. Do Not Change\n")
                while q1 not in ['1', '2', '3', '4']:
                    print("Invalid input. Please select 1, 2, 3, or 4.")
                    q1 = input("Make the meeting tone seem: \n1. Neutral\n2. Aggressive\n3. Positive\n4. Do Not Change\n")

                q2 = input("Change the formatting to be: \n1. More Verbose\n2. Less Verbose\n3. Do Not Change\n")
                while q2 not in ['1', '2', '3']:
                    print("Invalid input. Please select 1, 2, or 3.")
                    q2 = input("Change the formatting to be: \n1. More Verbose\n2. Less Verbose\n3. Do Not Change\n")

                q3 = input("Emphasize: \n1. Numbers\n2. Decisions\n3. Conflicts\n4. Do Not Change\n")
                while q3 not in ['1', '2', '3', '4']:
                    print("Invalid input. Please select 1, 2, 3, or 4.")
                    q3 = input("Emphasize: \n1. Numbers\n2. Decisions\n3. Conflicts\n4. Do Not Change\n")

                modification_commands = "Make the following modifications to the summary based on the transcript:\n"

                # Update modification_commands based on user inputs
                if q1 == '1':
                    modification_commands += "Set tone: Neutral\n"
                elif q1 == '2':
                    modification_commands += "Set tone: Aggressive\n"
                elif q1 == '3':
                    modification_commands += "Set tone: Positive\n"

                if q2 == '1':
                    modification_commands += "Change formatting: More Verbose\n"
                elif q2 == '2':
                    modification_commands += "Change formatting: Less Verbose\n"

                if q3 == '1':
                    modification_commands += "Emphasize: Numbers\n"
                elif q3 == '2':
                    modification_commands += "Emphasize: Decisions\n"
                elif q3 == '3':
                    modification_commands += "Emphasize: Conflicts\n"

        else:
            print("GPT Disabled")
            accepted = True


if __name__ == '__main__':
    main()