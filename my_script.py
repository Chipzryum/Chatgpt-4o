import os
from openai import OpenAI

# Set your GitHub token and endpoint
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

# Initialize the OpenAI client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Create a chat completion request
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

# Print the response
print(response.choices[0].message.content)
