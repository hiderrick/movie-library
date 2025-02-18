import openai

openai.api_key = api_key

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "Based on the user's input, generate a list of 5 movies that the user would like to watch."},
              
              ]
)

print(response["choices"][0]["message"]["content"])



