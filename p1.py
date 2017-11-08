import nltk
import re
import json
from pprint import pprint 
import treetaggerwrapper

#nltk.download('punkt') 
def leerArchivo():
    #leer el archivo       
    txt = open("ensenada.txt", encoding="utf-8").read()
    return(txt)

def oraciones():
    txt = leerArchivo()
    #Separar por oraciones
    sentences = nltk.tokenize.sent_tokenize(txt)
    print (sentences)
    return (sentences)

def tokens():
    sentences = oraciones()
    #Separar por tokens
    tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
    print(tokens)
    return (tokens)

def tagTokens():
    tokens = tokens()
    #Etiquetado de tokens
    pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
    print(pos_tagged_tokens)

def treeTagger():
    print("Inicia uso de TreeTagger: ")
    print()
    sentences = oraciones()
    
    #1) build a TreeTagger wrapper:
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='es',TAGDIR='C:/Users/DELL/Documents/7mo SEMESTRE/Manipulacion/NLTK/tree-tagger-windows-3.2/TreeTagger')

    tags = [tagger.tag_text(s) for s in sentences]
    pprint(tags)
    print()

    tags2 = [treetaggerwrapper.make_tags(t) for t in tags]
    pprint(tags2)

treeTagger()
