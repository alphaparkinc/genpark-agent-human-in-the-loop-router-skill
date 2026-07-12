class AgentHumanInTheLoopRouterClient:
    def route(self, confidence_score: float) -> dict:
        return {"route_target": "human_reviewer" if confidence_score < 0.6 else "agent_resolve"}