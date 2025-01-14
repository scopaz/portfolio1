from openai import OpenAI

# Authenticate the OpenAI client
client = OpenAI(
  api_key="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",
  organization='org-hKFYHkH1rBiaULYlSiRDbLcT',
  project='proj_pSY7kD0eI9X53Pxq0E32F50R',
)

# Create a chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hey GPT, greet me in a creative way."}
    ],
    max_tokens=1
)

# Print the response
print(completion["choices"][0]["message"]["content"])
