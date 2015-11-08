__author__ = 'Victor'

import urllib
#import re
import inflect
from nltk.stem.porter import PorterStemmer

#sentence = 'Don\'t be a fool for the city nights, I know it\'s cold but it\'s only light'
sentence = raw_input('Enter string that needs ASL translation: ')
sentence = sentence.lower()
sentence=sentence.replace('Don\'t','do-not')
junkWords = [' a ',' an ',' and ',' be ',' the ',' it\'s ',', ','\' ']
for junkWord in junkWords:
    sentence=sentence.replace(junkWord,' ')
print sentence

baseURL = 'http://www.handspeak.com/'
baseSearchURL = 'http://www.handspeak.com/word/search.php?wordID='

for word in sentence.split():
    fullSearchURL=baseSearchURL+word
    f = urllib.urlopen(fullSearchURL)
    for line in f.read().split("\n"):
        found=False
        if("video src" in line):
            endURL=line[12:]
            endURL=endURL[:endURL.index("\"")]
            fullURL=baseURL+endURL
            print 'getting video from'+fullURL
            found=True
            break
    if(found):
        urllib.urlretrieve(fullURL,word+'.mp4')
    else:
        p=inflect.engine()
        origword=word
        word=p.singular_noun(word)
        if(word!=False):
            fullSearchURL=baseSearchURL+word
            f = urllib.urlopen(fullSearchURL)
            for line in f.read().split("\n"):
                found=False
                if("video src" in line):
                    endURL=line[12:]
                    endURL=endURL[:endURL.index("\"")]
                    fullURL=baseURL+endURL
                    print 'getting video from'+fullURL
                    found=True
                    break
            if(found):
                urllib.urlretrieve(fullURL,word+'.mp4')
        else:
            p = PorterStemmer()
            word=PorterStemmer.stem_word(p,origword)
            fullSearchURL=baseSearchURL+word
            f = urllib.urlopen(fullSearchURL)
            for line in f.read().split("\n"):
                found=False
                if("video src" in line):
                    endURL=line[12:]
                    endURL=endURL[:endURL.index("\"")]
                    fullURL=baseURL+endURL
                    print 'getting video from'+fullURL
                    found=True
                    break
            if(found):
                urllib.urlretrieve(fullURL,word+'.mp4')
