from env.models import Observation, Action
from env.tasks import TASKS
from env.grader import grade
from sandbox.executor import run_code


class CodeDebugEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.index = 0
        self.step_count = 0
        return self._get_obs()

    def state(self):
        return self._get_obs()

    def step(self, action_dict):
        action = Action(**action_dict)
        task = TASKS[self.index]

        score, msg = grade(task, action.fixed_code)

        reward = max(score - 0.1, 0.0)

        self.index += 1
        self.step_count += 1

        done = self.index >= len(TASKS)

        return self._get_obs(), float(max(reward, 0.0)), done, {
    "msg": msg,
    "hint": "Check syntax, indentation, or logic errors",
    "improvement": "Fix the root cause of the error"
}

    def _get_obs(self):
        if self.index >= len(TASKS):
            return {
                "code": "",
                "error": "",
                "step": self.step_count,
                "difficulty": "done",
                "language": "python"
            }

        task = TASKS[self.index]

        success, error = run_code(task["code"], task.get("language", "python"))

        return Observation(
            code=task["code"],
            error=error if not success else "",
            step=self.step_count,
            difficulty=task["difficulty"],
            language=task.get("language", "python")
        ).dict()