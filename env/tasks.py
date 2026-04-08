import random

def generate_task(difficulty="easy"):
    if difficulty == "easy":
        return {
            "difficulty": "easy",
            "language": "python",
            "code": "print('Hello'",
            "expected_output": "Hello"
        }

    elif difficulty == "medium":
        n = random.randint(2, 5)
        return {
            "difficulty": "medium",
            "language": "python",
            "code": f"for i in range({n})\n    print(i)",
            "expected_output": "\n".join(str(i) for i in range(n))
        }

    elif difficulty == "hard":
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        return {
            "difficulty": "hard",
            "language": "python",
            "code": f"def add(a,b):\n    return a-b\nprint(add({a},{b}))",
            "expected_output": str(a + b)
        }


# fallback static tasks (for safety)
TASKS = [
    generate_task("easy"),
    generate_task("medium"),
    generate_task("hard")
]