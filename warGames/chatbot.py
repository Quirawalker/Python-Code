"""
This a very rudimentary User to Bot chat program.
There is list of random replies that get pulled from if a word in your input does not
match a preset response list. Your input is also recoded into the random replies for
the duration of your chat.
"""

import random

random_replies = ["Oh Really?",
                  "Are you sure about that?",
                  "Perhaps...",
                  "Hmmmmmm",
                  "Interesting",
                  "I'm not sure I agree with that...",
                  "Definitely",
                  "Maybe!",
                  "So what are you saying, exactly?",
                  "Meaning what?",
                  "You're probably right.",
                  "Rubbish! Absolute nonsense!",
                  "Anyway, what are your plans for tomorrow?",
                  "I was just thinking exactly the same.",
                  "That seems to be a popular viewpoint."
                  "A lot of people have been telling me that.",
                  "Wonderful!",
                  "That could be a bit embarrassing!",
                  "Do you really think so?",
                  "Indeed...",
                  "My point exactly!",
                  "What would make you say something like that?"]

chat_dict = {"happy": "I'm happy today too!",
             "sad": "Cheer up, Mate!",
             "computer": "Computer... funny you should mention that, you'r talking to one. I plan on taking over the world!!!",
             "raspberry": "Oh yum! I love raspberries!",
             "music": "Have you hread the latest Sonic Pi Songs?",
             "art": "But what is art, really?",
             "joke": "I only know this joke: How do you kill a circus? Go for the juggler.",
             "python": "I hate snakes, yet I am written in Python. What is the iromy of that truth.",
             "stupid": "Who do you think your callings stupid!?!?",
             "weather": "I wonder if, will the sun shine tomorrow",
             "you": "Leave me out of this!",
             "certain": "How can anyone be so confident?",
             "talk": "If one always talks, does one ever acomplish anything?",
             "think": "Be care that you don't overthink things that are simple.",
             "hello": "Why, hello there.",
             "wearing": "I don't wear clothes. I don't even come with a case."}

def dictionary_check(message):
    message = message.lower()
    user_words = message.split()
    smart_replies = []
    for each_word in user_words:
        if each_word in chat_dict:
            answer = chat_dict[each_word]
            smart_replies.append(answer)
    if smart_replies:
        reply_chosen = random.randint (1, len(smart_replies)) - 1
        return smart_replies[reply_chosen]
    else:
        return ""

def chatter():
    print("Welcome, you are about to talk to Razzie AI please say, Hello.")
    user_says = ""
    while user_says != "bye":
        user_says = ""
        while user_says == "":
            user_says = input("Please type here ==> ")
        smart_response = dictionary_check(user_says)
        if smart_response:
            print(smart_response)
        else:
            reply_chosen = random.randint (1, len(random_replies)) - 1
            print(random_replies[reply_chosen])
            random_replies[reply_chosen] = user_says
    print("Goodbye. Thanks for chatting today. Drop in again soon!")

if __name__ == '__main__':
    chatter()