import tkinter as tk
from tkinter import ttk
window=tk.Tk() 
window.title("Language Translator")
window.geometry("400x300")
from deep_translator import GoogleTranslator as Translator
def translate_text(text,source_lang,target_lang):
    translate=Translator(source=source_lang,target=target_lang)
    trans=translate.translate(text)
    return trans
label=tk.Label(window,text="Enter the text") #creates a label widget in the window with the text "Enter the text"
label.pack() #places the label in the window
text_input=tk.Entry(window) #creates an entry widget in the window for user input
text_input.pack() #places the entry widget in the window
source_Label=tk.Label(window,text="Enter the source language") #creates a label widget in the window with the text "Enter the source language"
source_Label.pack()
source_lang=ttk.Combobox(window,values=["en","es","fr","hi","de","ja"])
source_lang.pack()
target_Label=tk.Label(window,text="Enter the target language")
target_Label.pack()
target_lang=ttk.Combobox(window,values=["en","es","fr","hi","de","ja"])
target_lang.pack()
def translate():
    text=text_input.get()
    source=source_lang.get()
    target=target_lang.get()
    result=translate_text(text,source,target)
    result_Label.config(text=result)
button=tk.Button(window,text="Translate",command=translate)
button.pack()
result_Label=tk.Label(window,text="translated text will appear here")
result_Label.pack()   
window.mainloop() 