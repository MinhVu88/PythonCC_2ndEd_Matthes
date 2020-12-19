''' Messages: 
- Make a list containing a series of short text messages. 
- Pass the list to a function called show_messages(), which prints each text message
'''
lyrics = ['Augenballgroße Stücke vom Teig formen', 
          'Im Staubzucker wälzen und', 
          'sagt die Zauberwörter', 
          'Simsalbimbamba Saladu Saladim']

def show_messages(messages): 
    for message in messages: 
        print(f'\n{message}\n')

show_messages(lyrics)