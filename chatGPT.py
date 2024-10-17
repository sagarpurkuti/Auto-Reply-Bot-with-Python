import pyautogui
import time
import pyperclip
import openai
import os

# Set up the OpenAI API key securely
openai.api_key = os.getenv("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")

def is_last_message_from_sender(chat_log, sender_name="BreadFruit"):
    """
    Check if the last message in the chat log is from the specified sender.
    """
    messages = chat_log.strip().split("/2024")[-1]
    return sender_name in messages

def copy_chat_history(start_x, start_y, end_x, end_y):
    """
    Select and copy the chat history from the interface.
    """
    try:
        pyautogui.moveTo(start_x, start_y)
        pyautogui.mouseDown()
        pyautogui.moveTo(end_x, end_y, duration=1)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        return pyperclip.paste()
    except Exception as e:
        print(f"Error copying chat history: {e}")
        return None

def generate_response(chat_history):
    """
    Use OpenAI API to generate a response based on the chat history.
    """
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a person named Sagar who speaks Nepali as well as English. You are from Nepal and analyze chat history, responding like Sagar."},
                {"role": "user", "content": chat_history}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def paste_response(response, x, y):
    """
    Paste the generated response into the chat interface.
    """
    try:
        pyperclip.copy(response)
        pyautogui.click(x, y)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        # pyautogui.press('enter')  # Uncomment to automatically send the message
    except Exception as e:
        print(f"Error pasting response: {e}")

def main():
    # Define coordinates for clicking and selecting text
    icon_x, icon_y = 1248, 1043
    start_x, start_y = 726, 210
    end_x, end_y = 737, 927
    paste_x, paste_y = 930, 960

    # Step 1: Click on the icon to open chat
    pyautogui.click(icon_x, icon_y)
    time.sleep(2)

    while True:
        # Step 2: Copy chat history
        chat_history = copy_chat_history(start_x, start_y, end_x, end_y)
        if not chat_history:
            continue

        # Step 3: Check if the last message is from "BreadFruit"
        if is_last_message_from_sender(chat_history):
            # Step 4: Generate a response using OpenAI
            response = generate_response(chat_history)
            if response:
                # Step 5: Paste the generated response into the chat
                paste_response(response, paste_x, paste_y)

        # Wait a bit before the next iteration
        time.sleep(5)

if __name__ == "__main__":
    main()
