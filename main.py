# DigitalDeadHeads Agent v1.0
import os
import google.generativeai as genai

# 1. Setup the connection to Gemini using your Secret Key
# Make sure you named your Secret 'GEMINI_API_KEY' in Settings!
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in GitHub Secrets.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    def agent_think_tank():
        # This is the "Instruction" for your autonomous agent
        prompt = """
        You are the Lead Digital Artist for DigitalDeadHeads. 
        Write a 3-sentence vision for a 'Cyber-Stealie' logo update that blends 1960s art with 2026 tech.
        Then, write a specific question for Meta AI (Beta) asking it to 
        brainstorm how this logo would look if projected as a hologram in a VR concert space.
        """
        response = model.generate_content(prompt)
        return response.text

    if __name__ == "__main__":
        print("--- AGENT LOG START ---")
        thought = agent_think_tank()
        print(thought)
        print("--- AGENT LOG END ---")
