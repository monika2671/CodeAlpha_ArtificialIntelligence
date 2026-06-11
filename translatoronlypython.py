from deep_translator import GoogleTranslator as Translator
def translate_text(text,source_lang,target_lang):
    translate=Translator(source=source_lang,target=target_lang)
    trans=translate.translate(text)
    return trans
text=input("Enter the text to translate: ")
source_lang=input("Enter the source language: ")
target_lang=input("Enter the target language: ")
result=translate_text(text,source_lang,target_lang)
print("Translated text: ",result)