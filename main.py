import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

df = pd.read_csv("amazon.csv")

review_descriptions = df['review_content'].tolist()

sentiment_scores = []                                         

for description in review_descriptions[:20]:  # Limit to first 20 descriptions
    messages=[
    {"role": "system", "content": "You are a sentiment analysis model. Classify the sentiment of the given text as a number from 1 to 5, where 1 is very negative and 5 is very positive. Make your responses concise and only provide the number."},
    ]

    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": description}
    messages.append(user_dict) 
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=50
    )

    sentiment_scores.append(int(response.choices[0].message.content.strip()))  # Append the sentiment score to the list

print("Sentiment Scores: ", sentiment_scores)

# Add the sentiment scores to the DataFrame
df["Sentiment Score"] = sentiment_scores + [None] * (len(df) - len(sentiment_scores))  # Fill the rest with None

print(df[["Sentiment Score", "rating"]].head(20))  # Display the first few rows of the DataFrame with sentiment scores