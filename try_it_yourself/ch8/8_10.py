''' Sending Messages: 
- Start with a copy of your program from 8_9.py 
- Write a function called send_messages() that prints each text message and 
  moves each message to a new list called sent_messages as it’s printed. 
- After calling the function, print both of your lists to make sure the messages were moved correctly
'''
unsent_messages = ["I've got some advice for you, little buddy", 
                   "Before you point your finger, you should know that I'm the man", 
                   "If I'm the fuckin' man, then you're the fuckin' man as well", 
                   "So you can point that fuckin' finger up your ass"]

print('\n[ The unsent messages ]')

for msn in unsent_messages: print(f'\n\t- {msn}')

sent_messages = []

def send_messages(unsent, sent):
    while unsent: 
        sentMsn = unsent.pop()

        print(f"\n+ Sending '{sentMsn}' to sent_messages\n")
        
        sent.append(sentMsn)

        sent.reverse()   
            
def show_sent_messages(sent): 
    for msn in sent:
        print(f'\n\t* {msn}')

send_messages(unsent_messages, sent_messages)

print('\n[ The sent messages ]')

show_sent_messages(sent_messages)
