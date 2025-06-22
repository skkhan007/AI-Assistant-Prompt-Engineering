def get_prompts(option):
    if option == '1':
        return [
            "What is the capital of [insert text]?",
            "Can you explain the significance of [insert text]?",
            "Tell me three facts about [insert text]."
        ]
    elif option == '2':
        return [
            "Summarize the following article: [insert text]",
            "What are the main points of this text: [insert text]?",
            "Provide a brief overview of this document: [insert text]"
        ]
    elif option == '3':
        return [
            "Write a short story about [insert text].",
            "Create a poem about [insert text].",
            "Generate a creative idea for a story based on: [insert text]"
        ]
    else:
        return []
