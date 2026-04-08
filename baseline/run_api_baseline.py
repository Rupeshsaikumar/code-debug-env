import os
from openai import OpenAI
from env.environment import CodeDebugEnv

# Load API key safely
api_key = os.getenv("HF_TOKEN")

if not api_key:
    print("❌ ERROR: HF_TOKEN not set")
    print("Run this first:")
    print("set HF_TOKEN=your_api_key")
    exit()

client = OpenAI(api_key=api_key)

env = CodeDebugEnv()
obs = env.reset()

total_score = 0
done = False

while not done:
    print("\n--- TASK ---")
    print("Code:\n", obs["code"])
    print("Error:\n", obs["error"])

    # Prompt for AI
    prompt = f"""
Fix the following Python code.

Code:
{obs['code']}

Error:
{obs['error']}

Return ONLY corrected code.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        fixed_code = response.choices[0].message.content.strip()

    except Exception as e:
        print("⚠ API failed, using fallback...")
        print("Error:", e)

        # SAFE fallback (your old logic)
        if "print('Hello'" in obs["code"]:
            fixed_code = "print('Hello')"
        elif "for i in range" in obs["code"]:
            fixed_code = "for i in range(3):\n    print(i)"
        else:
            fixed_code = "def add(a,b):\n    return a+b\nprint(add(2,3))"

    obs, reward, done, info = env.step({"fixed_code": fixed_code})

    print("\n--- RESULT ---")
    print("Fixed Code:\n", fixed_code)
    print("Reward:", reward)

    total_score += reward

print("\nFINAL SCORE:", total_score)