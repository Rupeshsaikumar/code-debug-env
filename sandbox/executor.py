import subprocess
import tempfile
import os

def run_code(code, language="python"):
    try:
        suffix = ".py" if language == "python" else ".txt"

        with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as f:
            f.write(code)
            filename = f.name

        if language == "python":
            cmd = ["python", filename]
        else:
            return False, "Language not supported yet"

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=2
        )

        if result.returncode != 0:
            return False, result.stderr.strip()

        return True, result.stdout.strip()

    except subprocess.TimeoutExpired:
        return False, "Execution timeout"

    except Exception as e:
        return False, str(e)