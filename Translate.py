from googletrans import LANGUAGES
#for lang in LANGUAGES:
    #print(f'{lang} - {LANGUAGES[lang]}')


from googletrans import Translator
tran = Translator()
b=input("Enter the code for inputted word = ")
print()
print(f"The input will be taken as {LANGUAGES[b]}")
print()
a=input("Enter the word = ")

while 1:
 print ()
 c=input("Enter the code to get result = ")

 print(f"The output will be resulted as {LANGUAGES[c]}")
 print()
 t=tran.translate(a,src=b,dest=c)
 #print(f'Source: {t.src}')

 #print(f'Translation : {t.dest}')

 #print(f'Previous word = {t.origin}')
 #print()
 print(f'New translated word in {LANGUAGES[c]}= {t.text}')
