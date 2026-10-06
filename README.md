# Salon Marketing Matchmaking Agent - Proof of Concept

Animated demo of an AI agent that interviews a salon owner, a marketing freelancer,
and a marketing agency, then recommends the best match.

## Files

| File | Purpose |
| --- | --- |
| `simulation.html` | The interactive web simulation (main demo) |
| `serve_simulation.py` | Local web server that serves the simulation |
| `demo_simulation.html` | Static landing page explaining the matchmaking process |
| `README.md` | This file |

## How to Run

```bash
python3 serve_simulation.py
```

This starts a server on port 8080 and opens your browser at
`http://localhost:8080/simulation.html`. Press `Ctrl+C` to stop it.

You can also open `simulation.html` directly in a browser, though the
`demo_simulation.html` landing page links to it by relative path.

## Using the Simulation

- **Start Simulation** - runs the full conversation automatically
- **Pause / Resume** - freezes playback mid-conversation
- **Step Forward** - advances one line at a time, useful for walking an audience through it
- **Reset** - clears the panels and returns the agent to its starting position

The agent (🤖) travels between the three participant panels as it conducts each
interview, and a match recommendation appears at the end.

## Simulation Flow

### Phase 1: Salon Owner Context Gathering
- Salon: "Glow Up Salon" in Mumbai
- Objective: Diwali Instagram campaigns, budget under ₹15,000
- Preferences: Festive content, bridal makeup focus, video reels
- Timeline: Start in 2 weeks

### Phase 2: Freelancer Interview
- Name: Arjun, freelance social media manager
- Specialization: Beauty/wellness brands (15+ salons)
- Services: Content creation, community management, basic ads
- Pricing: ₹8,000/month (12 posts, 4 reels, weekly analytics)
- Availability: Immediate start, 2-3 day turnaround
- Experience: Successful Diwali campaigns (30-40% booking increase)

### Phase 3: Agency Interview
- Name: Neha from PixelPulse Marketing
- Specialization: Lifestyle brands, premium salons
- Services: Full-service marketing (strategy, content, ads, influencers)
- Pricing: ₹25,000/month salon starter package
- Capacity: Team of 5, 2-3 new clients/month
- Expertise: Festive campaigns, high-impact Diwali offers

### Phase 4: Match Recommendation
- Based on the salon's budget (₹15,000) and need for quick turnaround
- Freelancer selected (₹8,000/month fits budget)
- Agency exceeds budget (₹25,000/month)
- Agent facilitates the introduction

## Technical Notes

- Vanilla HTML/CSS/JavaScript - no frameworks, no build step, no dependencies
  beyond Python's standard library for the server.
- All conversations are hardcoded for this POC, as requested.
- The conversation steps live in the `steps` array in the `MatchmakingSimulation`
  class in `simulation.html`. Each entry is either a `move` (travel to a panel) or a
  `message` (a line of dialogue), with a `delay` in milliseconds.
- The agent's target position is resolved from each panel's real
  `getBoundingClientRect()`, so it stays aligned at any viewport size.

## Next Steps After POC Approval

1. Replace hardcoded responses with LLM-powered dynamic conversations
2. Generate questions dynamically based on context
3. Add profile databases for freelancers and agencies
4. Implement multi-factor matching (budget, style, availability, etc.)
5. Add negotiation and post-match relationship management
6. Implement the success-fee monetization model
