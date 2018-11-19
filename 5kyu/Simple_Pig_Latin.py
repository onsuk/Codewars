'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''


def pig_it(text):
    res = ''
    for spl in text.split():
        if spl=='!' or spl=='?':
            res = res + spl
        else:
            res = res + (spl + spl[0])[1:] + "ay" + " "

    return res.rstrip()