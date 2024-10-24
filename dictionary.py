import nltk
from nltk.corpus import wordnet as wn

# Download WordNet data
nltk.download('wordnet')

def get_definition(word):
    """Fetches the definition of a word from WordNet."""
    synsets = wn.synsets(word)
    if not synsets:
        return f"Sorry, I couldn't find a definition for '{word}'."
    
    # Return the first definition
    return synsets[0].definition()

def dictionary_chatbot():
    print("Welcome to the Dictionary Chatbot!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == 'exit':
            print("Chatbot: Goodbye see you soon!")
            break
        
        definition = get_definition(user_input)
        print(f"Chatbot: {definition}")

# Run the chatbot
dictionary_chatbot()
