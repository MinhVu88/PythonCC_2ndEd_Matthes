''' Archived Messages: 
- Start with 8_10.py 
- Call the function send_messages() with a copy of the list of messages. 
- After calling the function, print both of your lists to show that the original list has retained its messages
'''
unsent_messages = ["A child's rhyme stuck in my head", 
                   "It said that life is but a dream", 
                   "I've spent so many years in question", 
                   "To find I've known this all along"]

print('\n[ The unsent_messages list ]')

for msn in unsent_messages: print(f'\n\t- {msn}')

sent_messages = []

def send_messages(unsent, sent):
    while unsent: 
        sentMsn = unsent.pop()

        print(f"\n+ Sending '{sentMsn}' to sent_messages\n")
        
        sent.append(sentMsn + ' (Peyote)')

        sent.reverse()   
            
def show_sent_messages(sent): 
    for msn in sent:
        print(f'\n\t* {msn}')

send_messages(unsent_messages[:], sent_messages)

print('\n[ The sent_messages list ]')

show_sent_messages(sent_messages)

print('\n[ The original unsent_messages list ]')

for msn in unsent_messages: print(f'\n\t- {msn}')
