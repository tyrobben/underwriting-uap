import os
from contextual import ContextualAI
from dotenv import load_dotenv

load_dotenv()

def test_basic_retrieval():
    client   = ContextualAI()
    agent_id = os.environ["AGENT_ID"]
    r = client.agents.query.create(
        agent_id=agent_id,
        messages=[{"role": "user", "content": "Hazard index for welding?"}],
        top_k_retrieved_chunks=1,
    )
    assert len(r.retrieval.chunks) >= 1
