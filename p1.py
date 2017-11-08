import nltk
import re
import json

#nltk.download('punkt') 
def leerArchivo():
    #EOS detection        
    txt1 = open("ensenada.txt", "r")
    txt = txt1.read()
    return(txt)

def stopWords():
    with open('StopWords.txt') as document:
        stopWord = []
        for line in document:
            line = line.strip()
            if not line:
                continue
            stopWord.append(line)
    return stopWord

##def limpiarTxt():
##    array = leerArchivo()
##    stopWordd = stopWords()  
##    for i in range(len(array)):    
##        valor = array[i]
##        print(valor)
##        #ELIMINAR STOP WORDS
##        if valor in stopWordd:
##            valor = ''
##        #MINUSCULAS
##        valor = valor.lower()
##        #ACENTOS
##        valor= re.sub(r'[?|$|.|[|\\|!|  ]',r' ',valor)
##        valor= re.sub(r'[%|)|:|/|\"]',r' ',valor)
##        valor= re.sub(r'Ã¡|ã¡',r'a',valor)
##        valor= re.sub(r'Ã©',r'e',valor)
##        valor= re.sub(r'Ã\xad|ã\xad',r'i',valor)
##        valor= re.sub(r'ã³|Ó]',r'o',valor)
##        valor= re.sub(r'ãº|Ú]',r'u',valor)
##        valor= re.sub(r'[0-9]',r'',valor)
##        valor= re.sub(r'ã±|Ã±',r'ñ',valor)           
##        #ELIMINAR LOS @
##        if '@' in valor:
##            valor = ''   
##        #ELIMINAR LOS LINKS
##        if 'http' in valor:
##            valor = ''
##        #EMOJIS =caritas felices, corazones, 
##        valor= re.sub(r'â\x99¡|â\x98º',r'',valor)                 
##        array[i]=valor
##    print(array)
##    return(array)
##
txt = leerArchivo()    
#Separar por oraciones
sentences = nltk.tokenize.sent_tokenize(txt)
print (sentences)

print()

#Separar por tokens
tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
print(tokens)

print()

#Etiquetado de tokens
##nltk.download('averaged_perceptron_tagger') 
#Part Of Speech (POS) tagging
pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
print(pos_tagged_tokens)
print()

### From here using TreeTagger for Spanish tagging ###

from pprint import pprint  # For proper print of sequences.
import treetaggerwrapper

print("Inicia uso de TreeTagger: ")
print()
#1) build a TreeTagger wrapper:
tagger = treetaggerwrapper.TreeTagger(TAGLANG='es',TAGDIR='C:/Users/DELL/Documents/7mo SEMESTRE/Manipulacion/NLTK/tree-tagger-windows-3.2/TreeTagger')

tags = [tagger.tag_text(s) for s in sentences]
pprint(tags)
print()

tags2 = [treetaggerwrapper.make_tags(t) for t in tags]
pprint(tags2)
