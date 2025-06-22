import openai
from prompts import get_prompts

# Configure your OpenAI API key
openai.api_key = "your-api-key-here"  # Replace with your actual key

feedback_log = []

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def ask_feedback():
    fb = input("Was this response helpful? (yes/no): ").strip().lower()
    feedback_log.append(fb)

def main():
    while True:
        print("\nWelcome to Your AI Assistant!")
        print("1. Answer Questions")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '4':
            print("Thanks for using the assistant!")
            break

        prompts = get_prompts(choice)
        print("\nChoose a prompt style:")
        for i, p in enumerate(prompts, start=1):
            print(f"{i}. {p}")

        try:
            p_index = int(input("Choose prompt (1/2/3): ").strip()) - 1
            user_input = input("Enter your query or text:\n")

            selected_prompt = prompts[p_index].replace("[insert text]", user_input)
            response = get_ai_response(selected_prompt)

            print("\nAI Response:\n", response)
            ask_feedback()

        except Exception as e:
            print("Invalid input. Please try again.")

    # Save feedback
    with open("feedback_log.txt", "a") as f:
        for fb in feedback_log:
            f.write(fb + "\n")

if __name__ == "__main__":
    main()
