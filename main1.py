from hf import generate_response
import time

def temperature_prompt_activity():
    print("="*70)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE + INSTRUCTION")
    print("="*70)

    print("\nPart 1: Temperature EXPLORATION")
    base = input("Enter a creative prompt: ").strip()
    for t, label in [(0.1, "LOW (0.1) - Deterministic"),
                     (0.5, "MEDIUM (0.5) - Balanced"),
                     (0.9, "HIGH (0.9) - Creative")]:
        print(f"\n--- {label} ---")
        print(generate_response(base, temperature=t, max_tokens = 512))
        time.sleep(1)

    print("\nPart 2: INSTRUCTION-BASED PROMPTS")
    topic = input("Choose a topic (e.g., climate change, space exploration): ").strip()
    prompts = [
        f"Summurize key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from 2050 about {topic}.",
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\n--- INSTRUCTIONS {i} ---\n{p}")
        print(generate_response(p, temperature=0.7, max_tokens=512))
        time.sleep(1)
    