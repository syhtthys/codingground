print 'RISK VERDEDIG ADVIES'
print (' ')

while True:
     aantaldobs = 'nog niet echt bepaald'
     ogen = input('Wat zijn de hoogste twee getallen die de aanvaller heeft gegooid? ')
     lijssie =       [211,212,213,214,215,216,221,222,223,224,225,226,231,232,233,234,235,241,242,243,144,145,146,251,252,253,154,155,156,261,262,263,164,165,166,]
     for item in lijssie:
         if item-200 == ogen:
             aantaldobs = 'twee dobbelstenen.'
         if item-100 ==ogen:
             aantaldobs = 'een dobbelsteen.'

     print (' ')
     if aantaldobs=='nog niet echt bepaald':
        print 'Hahaha! Ok. Nu even serieus.'
        print'Weet je zeker dat de aanvaller met dobbelstenen gooit?'
     else:
        print"Ik adviseer je om je te verdedigen met", aantaldobs
     print (' ')