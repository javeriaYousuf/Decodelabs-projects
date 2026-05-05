# ============================================================
#   DecodeLabs | Batch 2026 | Project 2: Expense Tracker
#   Developer: Python Intern
#   Concepts:  Accumulator Pattern | Input Validation | Loops
# ============================================================

def main():
    print("=" * 45)
    print("   💰 DecodeLabs Expense Tracker - Project 2")
    print("=" * 45)
    print("  Enter expense amounts one at a time.")
    print("  Type 'quit' to stop and see your total.")
    print("-" * 45)

    total = 0          # Accumulator — initialized OUTSIDE the loop
    count = 0          # Track number of valid transactions

    while True:
        user_input = input("\n  Enter expense amount (or 'quit'): ").strip()

        # ── Kill Switch / Sentinel Value ──────────────────
        if user_input.lower() == "quit":
            break

        # ── Gatekeeper: Type Safety & Error Handling ──────
        try:
            expense = float(user_input)

            if expense < 0:
                print("  ⚠️  Invalid: Negative amounts not allowed.")
                continue

            # ── Accumulator Pattern ───────────────────────
            total += expense          # total = total + expense
            count += 1

            print(f"  ✅ Added: ${expense:,.2f}  |  Running Total: ${total:,.2f}")

        except ValueError:
            print("  ❌ Invalid Data — please enter a number (e.g. 100, 50.5).")

    # ── Phase 3: Output ───────────────────────────────────
    print("\n" + "=" * 45)
    print("            📊 FINAL REPORT")
    print("=" * 45)
    print(f"  Transactions recorded : {count}")
    print(f"  TOTAL SPENT           : ${total:,.2f}")
    print("=" * 45)
    print("  DecodeLabs | Batch 2026 — Audit Complete ✅")
    print("=" * 45)

if __name__ == "__main__":
    main()