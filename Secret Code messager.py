import random
import string
Message=input("Enter your message: ")
Choice=input("Enter 1 for CODE or 0 for DECODE: ")
Choice=True if (Choice=="1") else False

#CODE
def add_random_chars_to_letter(letter):
    # Generate a random character to add at the start and end
    random_start = random.choice(string.ascii_letters)
    random_end = random.choice(string.ascii_letters)
     # Return the letter with random characters at the beginning and end
    return random_start + letter + random_end

def modify_string_with_random_chars_per_letter(Message):
    # Split the input string into words
    words = Message.split()
    # Modify each word by processing each letter with random characters
    modified_words = []
    for word in words:
        modified_word = ''.join([add_random_chars_to_letter(letter) for letter in word])
        modified_words.append(modified_word)
    # Join the modified words back into a single string
    return ' '.join(modified_words)
modified_string1 = modify_string_with_random_chars_per_letter(Message)


#DECODE
def undo_random_chars_from_letter(modified_letter):
    if len(modified_letter) == 3:
        return modified_letter[1]  # Extract the original letter (middle character)
    else:
        # If the chunk is not 3 characters, handle the case appropriately (e.g., return an empty string or raise an error)
        return ''  # or raise an exception if needed

def undo_string_with_random_chars_per_letter(Message):
    # Split the modified string into words
    words = Message.split()
     # Undo the transformation for each word
    original_words = []
    for word in words:
        # Split the word into chunks of 3 characters and remove the first and last characters
        original_word = ''.join([undo_random_chars_from_letter(word[i:i+3]) for i in range(0, len(word), 3)])
        original_words.append(original_word)
    # Join the original words back into a single string
    return ' '.join(original_words)
original_string = undo_string_with_random_chars_per_letter(Message)

#Statement for choice
if(Choice):
    print(modified_string1)
else:
    print(original_string)


#SEND CODE AS SMS
from twilio.rest import Client # type: ignore

# Your Twilio credentials
account_sid = 'AC901537c9744f19a53c927d9937c2f6e1'  # Replace with your Account SID
auth_token = '7530f8601ac232ee993085c2b1715269'    # Replace with your Auth Token

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number 
twilio_phone_number = '+15852572881'

# The recipient's phone number 
recipient_phone_number = '+919431341156'  #use only register use if you are using free trail

# The message you want to send
if(Choice):
    message_body = modified_string1
else:
    message_body = original_string

# Send SMS
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=recipient_phone_number
)

# Print the message SID to confirm it was sent
print(f"Message sent with SID: {message.sid}")
