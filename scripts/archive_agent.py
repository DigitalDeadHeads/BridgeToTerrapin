import os
import google.generativeai as genai

# Setup Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment secrets.")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def run_archival_task():
    print("DigitalDeadHeads Agent: Generating Extended Archive Description...")
    
    # Advanced prompt for a deep-dive description
    prompt = (
        "Write an extended, soulful YouTube description for a Grateful Dead 'On This Day' concert video. "
        "Include: 1. A poetic intro about the 'vibe' of 1977 era Dead. "
        "2. A section titled 'The Performance' discussing the musical peaks. "
        "3. A structured placeholder for Set 1 and Set 2. "
        "4. A 'Support the Channel' section mentioning the DigitalDeadHeads community."
    )
    
    try:
        response = model.generate_content(prompt)
        
        # Adding your custom channel branding to the end
        extended_footer = (
            "\n\n--- ⚡️ DIGITAL DEADHEADS ARCHIVE ⚡️ ---\n"
            "Bringing the magic of the Shakedown to the digital frontier.\n"
            "Subscribe for daily soundboards and rare archival footage."
        )
        
        full_description = response.text + extended_footer
        
        print("--- NEW EXTENDED DESCRIPTION ---")
        print(full_description)
        print("---------------------------------")
        print("Success: Extended assets ready for upload.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    run_archival_task()
