import openai

# Initialize the OpenAI client with your API key
openai.api_key = "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"
command='''

[4:05 pm, 30/09/2024] purkuti101sagar: Excuse me
[4:05 pm, 30/09/2024] purkuti101sagar: yes pleaes
[8:09 pm, 12/10/2024] Bishal Rca: shall we go visit temple?
[8:09 pm, 12/10/2024] purkuti101sagar: 

'''
# Make a request to the OpenAI API to generate a completion
completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a person named sagar who speaks nepali as well as english. He is from Nepal and is a code. you analyze chat history and respond like sagar "},
        {"role": "user", "content": command}
    ]
)

# Print the response
print(completion.choices[0].message.content)


