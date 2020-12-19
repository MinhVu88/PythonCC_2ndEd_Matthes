glossary = {'ddos': 'a denial-of-service attack',
            'botnet': 'a number of Internet-connected devices, each of which is running 1 or more bots',
            'sql_injection': 'a code injection technique that might destroy your database',
            'rootkit': 'a collection of malicious software tools',
            'honeypot': 'a computer system that is set up to act as a decoy to lure cyberattackers'}

glossary['brute_force_attack'] = 'a trial-and-error method used to obtain info such as a user password or personal identification number (PIN)'
glossary['trojan_horse'] = 'a program that appears harmless, but is, in fact, malicious'
glossary['keylogger'] = 'a simple software that records the key sequence and strokes of your keyboard into a log file on your machine'
glossary['phishing'] = 'a hacking technique using which a hacker replicates the most-accessed sites and traps the victim by sending that spoofed link'
glossary['waterhole_attack'] = 'hackers target the most accessed physical location to attack the victim'

for word, meaning in glossary.items():
    print('\nThe meaning of ' + word + ':')
    print('\t' + meaning)