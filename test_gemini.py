"""Pre-cohort check for the Module 4.1 Gemini examples.

Run:  python test_gemini.py
Needs: pip install -U google-genai   and the GEMINI_API_KEY environment variable.
"""
import os
import sys

MODEL = "gemini-3.8-flash"   # the model used in Modules 4.1-4.4 and 5.1

if not os.environ.get("GEMINI_API_KEY"):
    sys.exit("GEMINI_API_KEY is not set. See step 3 of the instructions.")

try:
    from google import genai
except ImportError:
    sys.exit("The google-genai package is missing. Run: pip install -U google-genai")

client = genai.Client()

print(f"Test 1: system instruction ({MODEL})")
interaction = client.interactions.create(
    model=MODEL,
    system_instruction=(
        "You are a patient maths tutor for SHS students in Ghana. "
        "Explain one step at a time and use cedis in word problems."
    ),
    input="How do I solve 2x + 5 = 17?",
)
print(interaction.output_text, "\n")

print("Test 2: thinking level")
interaction = client.interactions.create(
    model=MODEL,
    input="Classify this SMS as SCAM or NOT_SCAM. Reply with one word.\n\n"
          "'Congratulations! You have won GHS 5,000. Send your MoMo PIN to claim.'",
    generation_config={"thinking_level": "low"},
)
print(interaction.output_text, "\n")

print("Both tests ran. The Module 4.1 examples work with your key.")
