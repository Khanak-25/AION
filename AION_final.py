import base64
import json
import os
import time

# ==============================
# 🧠 AION - The Secure AI Network
# ==============================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def encode_message(msg):
    return base64.b64encode(msg.encode()).decode()

def decode_message(encoded):
    return base64.b64decode(encoded.encode()).decode()

def load_memory():
    memory_file = "aion_memory.json"
    if not os.path.exists(memory_file):
        return []  # no file yet
    try:
        with open(memory_file, "r") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except Exception:
        return []  # if file is empty or broken

def save_memory(entry):
    memory_file = "aion_memory.json"
    data = load_memory()
    data.append(entry)
    with open(memory_file, "w") as f:
        json.dump(data, f, indent=4)

def show_memory():
    data = load_memory()
    if not data:
        print("🧠 No memory found yet.")
        return
    print("\n=== AION MEMORY ===")
    for i, entry in enumerate(data[-5:], 1):
        print(f"{i}. {entry['user']} → {entry['aion']}")
    print("===================\n")

# ------------------------------
# 💫 MAIN TERMINAL SIMULATION
# ------------------------------
clear()
slow_print("🔮 Initializing AION Quantum Network...", 0.05)
time.sleep(1)
slow_print("✅ System online. Quantum-safe channel established.", 0.04)
print("\nType your message or use commands: 'memory', 'clear', 'exit'\n")

while True:
    user = input("🧍 You: ").strip()
    if user.lower() == "exit":
        slow_print("👋 Shutting down AION node. Goodbye.", 0.04)
        break
    elif user.lower() == "memory":
        show_memory()
        continue
    elif user.lower() == "clear":
        clear()
        continue

    encoded = encode_message(user)
    reply = f"AION Node: Securely received your thought — [{encoded}]"
    slow_print(reply, 0.03)

    save_memory({"user": user, "aion": encoded})
