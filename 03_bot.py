
import pyautogui
import time
import pyperclip
import openai

openai.api_key = "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"


# while True:
# Step 1: Click on the icon at (1248, 1043)
icon_x, icon_y = 1248, 1043
pyautogui.click(icon_x, icon_y)

# Step 2: Wait for a short duration if needed (allowing time for window to open, etc.)
time.sleep(1)

# Step 3: Drag to select the text (from (669, 134) to (1896, 993))
start_x, start_y = 726, 210
end_x, end_y = 737, 927

pyautogui.moveTo(start_x, start_y)  # Move to the start point
pyautogui.mouseDown()               # Press the mouse button
pyautogui.moveTo(end_x, end_y, duration=1)  # Drag to the end point
pyautogui.mouseUp()                 # Release the mouse button

# Step 4: Copy the selected text (Ctrl+C or Command+C for Mac)
pyautogui.hotkey('ctrl', 'c')  # Use 'command' on Mac if necessary
pyautogui.click(930,960)
# Step 5: Wait for the clipboard to update
time.sleep(0.5)

# Step 6: Get the copied text from the clipboard using pyperclip
chat_history = pyperclip.paste()

# Step 7: Print or store the copied text in a variable
print("Copied Text: ", chat_history)


completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a person named sagar who speaks nepali as well as english. you are from Nepal and  a code. you analyze chat history and respond like sagar "},
        {"role": "user", "content": chat_history}
    ]
)

response=completion.choices[0].message.content
pyperclip.copy(response)

# Step 8: Click at the target location (930, 960)
pyautogui.click(930, 960)
time.sleep(1)

# Step 9: Paste the text (Ctrl+V or Command+V for Mac)
pyautogui.hotkey('ctrl', 'v')  # Use 'command' on Mac if necessary
time.sleep(1)


# Step 10: Press Enter to send the message
pyautogui.press('enter')