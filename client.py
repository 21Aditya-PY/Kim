from openai import OpenAI

client = OpenAI(
    api_keys="sk-proj-2o92Dj3FUsml7pY5m7DUT3BlbkFJK0is8WjluJ2YyIOiHfQ0",
) 


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named hagrid, skilled in general tasks like Alexa and Google Cloud."},
    {"role": "user", "content": "What is coding?."}
  ]
)

print(completion.choices[0].message.content)