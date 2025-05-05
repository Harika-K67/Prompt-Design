from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Initialize OpenAI client with API key from environment
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# Three versions of prompts to summarize the same news article
prompts = [
    # Prompt 1: Minimal prompt
    "Summarize this article.",

    # Prompt 2: Standard prompt with clearer intent
    "Summarize the main ideas and key takeaways from the following news article in 2-3 sentences",

    # Prompt 3: Highly structured prompt with explicit instruction
    "You are summarizing this article for a daily news digest. Write 2-4 sentences that cover the central issue, its broader implications, and notable reactions. Use an informative and engaging tone for non-expert audience."
]

article = """
OPEC+ will hold a rescheduled meeting on Saturday to determine its oil output policy for June, ahead of the original Monday schedule. Eight member countries are set to discuss whether to implement a further accelerated production hike or adhere to a previously planned smaller increase. This follows Saudi Arabia's push for a significant increase in May, which contributed to a decline in oil prices to a four-year low under $60 per barrel. The group is considering an increase of 411,000 barrels per day, three times the amount agreed upon in December. Tensions have arisen due to Iraq and Kazakhstan reportedly exceeding their output targets, frustrating Riyadh. Despite market uncertainties and falling prices, some group members support a continued aggressive output hike. OPEC+, which includes both OPEC members and allies like Russia, is currently cutting over 5 million barrels per day in total. The full ministerial meeting of the group is scheduled for May 28. Market analysts suggest sticking closer to the existing output taper plan but acknowledge the possibility of unexpected changes by the producer alliance.
"""

# Run each prompt through the API and print output
for i, prompt in enumerate(prompts, 1):
    print(f"\n--- Prompt {i} ---")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": f"{prompt}\n\n{article}"}
        ]
    )
    print(response.choices[0].message.content)


