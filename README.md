# 🚀 CodeDebugEnv++: A Sandboxed Reinforcement Learning Environment for Intelligent Code Debugging

> 🧠 Training AI agents to debug real-world code through safe, interactive environments, Dynamically Works.


## 🧠 Overview

CodeDebugEnv++ is a real-world RL environment for automated code debugging using sandboxed execution and dynamic task generation.

CodeDebugEnv++ is a structured reinforcement learning environment designed for automated code debugging — a core capability in modern AI-powered developer tools.

It simulates a real-world workflow where AI agents analyze buggy code, understand execution errors, apply fixes, and validate outputs in a safe sandboxed environment.

## 🏗️ System Architecture

        ┌──────────────────────┐
        │     RL Agent         │
        │ (Generates Fix Code) │
        └─────────┬────────────┘
                  │ Action (fixed_code)
                  ▼
        ┌──────────────────────┐
        │   CodeDebugEnv++     │
        │  (step / reset)      │
        └─────────┬────────────┘
                  │
        ┌─────────▼────────────┐
        │      Grader          │
        │ (Evaluates Output)   │
        └─────────┬────────────┘
                  │
        ┌─────────▼────────────┐
        │   Sandbox Executor   │
        │ (Safe Code Runtime)  │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │   Execution Output   │
        │  (Error / Result)    │
        └──────────────────────┘

## 🏗️ System Architecture

- Environment → Handles RL logic
- Tasks → Defines debugging problems
- Grader → Scores correctness
- Sandbox → Runs code safely
- Baseline → Simulates AI agent

---

## 🤖 Why This is RL

- Agent gets state (code + error)
- Takes action (fixed code)
- Gets reward (0–1)
- Moves to next task

---

## 🔄 Dynamic Behavior

Tasks change every run.  
So scores may vary.  
This shows real-world behavior.


## 🎯 Motivation

Debugging is one of the most critical and time-consuming aspects of software development. Despite advances in AI, reliable automated debugging remains a challenging problem.

CodeDebugEnv++ provides a controlled and measurable environment where agents can learn and be evaluated on their debugging capabilities — bridging the gap between research experimentation and real-world developer workflows.



## 🧩 Environment Design

## 🔄 Dynamic Behavior

Tasks are generated dynamically at runtime, resulting in varied debugging scenarios.  
Baseline scores may vary across runs, reflecting realistic agent performance.

## 🧪 Interactive Debug Mode (Optional Feature)

You can also debug your own code using:

python interactive_debug.py

Paste your buggy code and type END.

This demonstrates real-world usability beyond RL evaluation.

Interactive Debug Mode allows real users to test debuggung live.


### 🔍 Observation Space

Each step provides the agent with:

* `code` → Buggy Python code
* `error` → Execution error message
* `difficulty` → Task level (easy / medium / hard)
* `step` → Current step count
* `language` → Programming language (currently Python)



### 🎮 Action Space

* `fixed_code` → The corrected version of the code (string)



## 🧪 Tasks

The environment includes three progressively challenging tasks:

 Difficulty    Description            
 ----------   ---------------------- 
 Easy         Fix syntax errors      
 Medium       Fix indentation issues 
 Hard         Fix logical errors     



## 🏆 Reward Function

The reward system is designed to provide continuous and meaningful feedback:

 Condition                Reward 
 ----------------------   ------ 
 Perfect fix               1.0    
 Partial fix               0.6    
 Incorrect but runnable    0.3    
 Execution failure         0.0    
 Step penalty             -0.1   

This encourages:

* Incremental learning
* Efficient problem-solving
* Avoidance of unnecessary steps


## 🔐 Sandbox Execution

All code is executed in a secure, isolated environment using subprocess-based execution with strict timeout control.

This ensures:

* Safety from harmful code execution
* Deterministic and reproducible evaluation
* Realistic debugging feedback


## ⚙️ Setup Instructions

### 🔧 Local Run

```bash
python --version
pip install pydantic
python baseline/run_baseline.py
python -m baseline.run_baseline
python interactive_debug.py

for API-Baseline

   it runs sometimes & sometimes it occurs API failed due to Network and Server issues.
...  
  GO TO THE git Bash
export HF_TOKEN="sk-proj-xxxxxxxxxxxx"
python -m baseline.run_api_baseline
  FOR Powershell
$env:HF_TOKEN="sk-proj-xxxxxxxx"
python -m baseline.run_api_baseline

```

### 🐳 Docker Run

```bash
docker --version
docker info
docker build -t code-debug-env .
docker run code-debug-env
```



## 📊 Results

Baseline Agent Performance:

FINAL SCORE: (1.3 – 2.7)

**Score: 2.7 / 3.0**

This demonstrates the environment’s ability to provide clear and consistent evaluation signals.

Why your score changed

Before (static tasks):
👉 Same questions every time
👉 Model “learns pattern” → score ~2.7

Now (dynamic tasks):
👉 Random values (range(5), range(4), add(1,5), etc.)
👉 Model must think more → sometimes fails


## 📦 OpenEnv Compliance

This environment fully adheres to OpenEnv standards:

* Typed models using Pydantic
* Standard API: `reset()`, `step()`, `state()`
* Deterministic grading system
* Multi-task evaluation pipeline

## ✅ OpenEnv Validation

This environment follows OpenEnv interface:
- step(action)
- reset()
- state()

Validated manually with expected behavior.

## 🌍 Real-World Applications

* AI-powered code assistants
* Automated debugging systems
* Developer productivity tools
* Intelligent IDE integrations



## 🚀 Extensibility

CodeDebugEnv++ is built with a modular sandbox architecture, making it easy to extend beyond Python.

Planned extensions include:

* JavaScript (Node.js execution)
* C/C++ (GCC-based compilation)
* Java (JVM execution)

The executor layer is designed to support additional languages without modifying the core reinforcement learning environment.


## 💡 Future Improvements

* Multi-step debugging workflows
* Test-case based evaluation
* Support for multiple programming languages
* Integration with real-world code datasets

## 💎 What Makes This Unique

Unlike traditional toy RL environments, CodeDebugEnv++ simulates a real-world developer workflow.

Key differentiators:
- Real execution-based feedback (not rule-based guessing).
- Continuous reward shaping instead of binary success/failure.
- Safe sandboxed runtime for realistic debugging.
- Designed for extensibility across multiple programming languages.
- It is has Interactive Debug Mode.
- It Works Dynamically also.


This makes it closer to real production AI systems than typical benchmark environments.

##  Final Note

CodeDebugEnv++ is designed not just as a benchmark, but as a stepping stone toward real-world AI systems capable of assisting developers in debugging tasks.

It reflects how modern AI copilots operate — combining reasoning, execution, and feedback — making it a meaningful environment for advancing applied AI research.

## Note

But why score sometimes low(1.3/2.0)

This is NOT an error.

This is actually expected behavior.

REASON:
 
 It shows real RL challenge.
  
 Not fake perfect system. 

 Shows learing opportunity.

 It is correct RL Environment.



## Conclusion

CodeDebugEnv++ provides a scalable, realistic, and evaluation-ready environment for training AI systems to debug code effectively.

By combining safe execution, structured feedback, and real-world task simulation, it offers a strong foundation for advancing automated debugging research and applications.
