'''#Write a function that prompts the user to enter a paragraph of text.
  Store the input text in a variable for further processing.'''
def get_user_paragraph():
    paragraph = input("Enter a paragraph of text: ")
    return paragraph

# Get user input
user_input = get_user_paragraph()

# Process the input
print("Length of the paragraph:", len(user_input))
