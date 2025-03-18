import time

def get_user_input(prompt):
    """Prompt the user for input and return the entered value."""
    return input(prompt).strip()

def build_story(adjective, noun, verb, adverb):
    """Construct and return a Mad Libs story using f-string formatting."""
    return (
        f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
        "I couldn't believe my eyes!"
    )

def play_mad_libs():
    """Runs the Mad Libs game once, collecting input and displaying the story."""
    print("\nWelcome to Python Mad Libs!")
    print("Answer the following questions to create your very own silly story.\n")

    # Get user inputs
    adjective = get_user_input("Enter an adjective: ")
    noun = get_user_input("Enter a noun: ")
    verb = get_user_input("Enter a verb: ")
    adverb = get_user_input("Enter an adverb: ")

    # Build and display the story
    story = build_story(adjective, noun, verb, adverb)
    print("\nHere is your story:")
    print(story)

def main():
    """Main function to run the game and ask if the user wants to play again."""
    while True:
        play_mad_libs()
        replay = get_user_input("\nWould you like to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            time.sleep(1)  # Short pause before exiting
            break

if __name__ == "__main__":
    main()
