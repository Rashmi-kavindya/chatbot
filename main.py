import re
import long_responses as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    # Calculate the percentage of recognized words in user message
    percentage = float(message_certainty) / float(len(recognized_words)) if recognized_words else 0

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    
def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response --------------------------------
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response("I'm doing fine, and you?", ['how', 'are', 'you', 'doing'], required_words=['how', 'are', 'you'])

    if highest_prob_list:
        best_match = max(highest_prob_list, key=highest_prob_list.get)
        print(highest_prob_list)  
        return best_match
    else:
        return "I'm not sure what you mean."

def get_responses(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())  # Fixed regex
    response = check_all_messages(split_message)
    return response if response else "I don't understand."

# Testing the responses system
while True:
    user_input = input('You: ')
    bot_response = get_responses(user_input)
    print('Bot:', bot_response)
