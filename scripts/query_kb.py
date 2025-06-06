#!/usr/bin/env python
import os, json
from contextual import ContextualAI
from dotenv import load_dotenv

load_dotenv()

client   = ContextualAI()                         # key auto-loads from env
AGENT_ID = os.environ["AGENT_ID"]

print("Ask any underwriting question and press Enter.")
question = input("→ ")

response = client.agents.query.create(
    agent_id = AGENT_ID,
    messages = [ { "role": "user", "content": question } ],
    top_k_retrieved_chunks = 4,                   # optional, default = 10
    include_metadata       = True,
)

print(json.dumps(response.to_dict(), indent=2))
