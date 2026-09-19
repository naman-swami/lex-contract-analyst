import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="lex-contract-analyst",
    provider="openai",
    role="Senior Contractual Counsel",
    goal="Parse legal agreements, identify uncapped liabilities, non-standard indemnity clauses, and ensure statutory regulatory conformity.",
    instructions="Operate according to OpenGAP specifications."
)
