glossary = {'ddos': 'a denial-of-service attack',
            'botnet': 'a number of Internet-connected devices, each of which is running 1 or more bots',
            'sql_injection': 'a code injection technique that might destroy your database',
            'rootkit': 'a collection of malicious software tools',
            'honeypot': 'a computer system that is set up to act as a decoy to lure cyberattackers'}

for word, meaning in glossary.items():
    print('\nThe meaning of ' + word + ':')
    print('\t' + meaning)