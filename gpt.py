import openai
import config

def initialize_gpt(API_KEY):
    """
    Initializes GPT with the key. Run before running any other GPT related functions.
    """
    openai.api_key = API_KEY

def initialize_system_prompt(SYSTEM_PROMPT, TRANSCRIPT_PATH):
    """
    Initializes the conversations list with system instructions containing the system prompt and the transcript content.

    Args:
    - SYSTEM_PROMPT (str): The system prompt text to be injected.
    - TRANSCRIPT_PATH (str): The path to the transcript file to read from.

    Returns:
    - conversations (list): The list of conversation objects to be fed back and used in further entry calls.
    """
    conversations = []

    with open(TRANSCRIPT_PATH, 'r') as file:
        transcript = file.read()
    
    conversations.append({'role': 'system', 'content': SYSTEM_PROMPT + "\n The following is the meeting transcript: \n" + transcript})
    return conversations

def request_response(MODEL_ID, TEMPERATURE, PRESENCE_PENALTY, conversation_log):
    """
    Performs conversation completion using OpenAI's Chat API.
    Reads the conversation log and generates a response and a new conversation log.

    Args:
    - conversation_log (list): A list of conversation objects representing the conversation history.

    Returns:
    - tokens (int): The total number of tokens used in the API response.
    - conversation_log (list): The updated conversation log with the new response appended.
    """
    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        temperature=TEMPERATURE,
        presence_penalty=PRESENCE_PENALTY,
        messages=conversation_log
    )
    
    conversation_log.append({
        'role': response.choices[0].message.role,
        'content': response.choices[0].message.content.strip()
    })
    
    tokens = response.usage['total_tokens']
    return tokens, conversation_log

def process_summarization_query(MODEL_ID: str, TEMPERATURE: float, PRESENCE_PENALTY: float, conversation_log: list, summarization_command: str, summary: str, modification_commands: str):
    """
    Processes a summarization query by injecting the summarization command, summary, and modification 
    commands as a user command and then requesting a new entry response from the GPT API.

    Args: 
    - conversation_log (list): A list of conversation objects representing the conversation history.

    Returns:
    - str: The updated summary.
    """ 
    conversations.append({'role': 'user', 'content': summarization_command + "\n" + summary + "\n" + modification_commands})
    tokens, conversations = request_response(MODEL_ID, TEMPERATURE, PRESENCE_PENALTY, conversations)
    return f"SUMMARY: {conversations[-1]['content'].strip()}\n"

if __name__ == '__main__':
    conversations = []
    api_key = input("API KEY: ")
    initialize_gpt(api_key)
    conversations = initialize_system_prompt(config.SYSTEM_PROMPT, 'debug_examples\sample_transcript_2.txt')
    response = process_summarization_query("gpt-3.5-turbo", 0.2, -0.2, conversations, """This is a decision making meeting.
Summarize the meeting transcript and create minutes that follow this template:
- List of all present meeting members
- Decisions Made
- Next Steps Planned
- Identification and Tracking of Action Items""")
    print(response)