from sandbox.executor import run_code

print("🔧 Interactive Debug Mode")
print("Paste your buggy code below.")
print("Type END (in new line) to run.\n")

lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)

code = "\n".join(lines)

print("\n⚡ Running your code...\n")

success, output = run_code(code)

print("----- RESULT -----")
if success:
    print("✅ Output:\n", output)
else:
    print("❌ Error:\n", output)