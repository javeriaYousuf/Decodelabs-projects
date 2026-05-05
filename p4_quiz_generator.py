
#   GENERAL KNOWLEDGE QUIZ
#   Topic: Geography (Capitals & Countries)

score = 0  # State Initialization

print("=" * 45)
print("   🌍 WELCOME TO THE GEOGRAPHY QUIZ! 🌍")
print("=" * 45)
print("  Answer 5 questions. Good luck!\n")

# ── Question 1 ──────────────────────────────
answer = input("Q1: What is the capital of France? ").strip().lower()
if answer == "paris":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The answer is: Paris\n")

# ── Question 2 ──────────────────────────────
answer = input("Q2: What is the capital of Japan? ").strip().lower()
if answer == "tokyo":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The answer is: Tokyo\n")

# ── Question 3 ──────────────────────────────
answer = input("Q3: Which country has the largest land area in the world? ").strip().lower()
if answer == "russia":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The answer is: Russia\n")

# ── Question 4 ──────────────────────────────
answer = input("Q4: What is the capital of Australia? ").strip().lower()
if answer == "canberra":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The answer is: Canberra\n")

# ── Question 5 ──────────────────────────────
answer = input("Q5: Which country does the River Nile primarily flow through before reaching the sea? ").strip().lower()
if answer == "egypt":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The answer is: Egypt\n")

# ── Final Score ─────────────────────────────
print("=" * 45)
print(f"  🏁 QUIZ COMPLETE!")
print(f"  Your final score: {score:>2} / 5")

if score == 5:
    print("  🌟 Perfect score! You're a Geography Pro!")
elif score >= 3:
    print("  👍 Good job! Keep learning!")
else:
    print("  📚 Keep practicing — you'll get there!")

print("=" * 45)