import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from env.environment import CodeDebugEnv

env = CodeDebugEnv()
obs = env.reset()

total_score = 0
done = False

while not done:
    print("\n--- TASK ---")
    print("Code:\n", obs["code"])
    print("Error:\n", obs["error"])

    # deterministic baseline
    if "print('Hello'" in obs["code"]:
        fixed = "print('Hello')"
    elif "for i in range(3)" in obs["code"]:
        fixed = "for i in range(3):\n    print(i)"
    else:
        fixed = "def add(a,b):\n    return a+b\nprint(add(2,3))"

    obs, reward, done, info = env.step({"fixed_code": fixed})
    print("\n✅ RESULT:")
    print("✔ Reward:", round(reward,2))
    print("💬 Message:", info.get("msg"))
    print("💡 Hint:", info.get("hint","Fix syntax/logic"))

    
    total_score += reward

print("\nFINAL SCORE:", total_score)