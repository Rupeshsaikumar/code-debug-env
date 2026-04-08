from sandbox.executor import run_code

def grade(task, action_code):
    success, output = run_code(action_code)

    # Perfect match
    if success and output == task["expected_output"]:
        return 1.0, "Perfect fix"

    # Partial match
    if success and output.strip() in task["expected_output"]:
        return 0.6, "Partially correct"

    # Runs but wrong
    if success:
        return 0.3, "Runnable but incorrect"

    # Failed execution
    return 0.0, "Execution failed"