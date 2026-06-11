import tkinter as tk
from tkinter import ttk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
faqs={"What is programming?":"Programing is a process is creating a set of instructions that computer follows to perform tasks",
"What are the different programming languages?":"There are many languages including python, java, c++ etc",
"What is python":"Python is a high level,interpreted programming language know for its easy syntax and versatility.",
"Uses of python":"Python is used in web development, data analysis, machine learning, automation and more.",
"How to learn programming?":"You can start by choosing a programming language, watching tutorials online, practicing coding "
"exercises and building projects",
"Is programming difficult?":"Programming can be challenging at first, but with practice and persistence, it becomes easier.",
"Can programming be a career?":"Yes, programming can be a rewarding career with many job opportunities in various industries."}
def preprocess(text):
    text=text.lower().strip() #converts text to lowercase and removes leading/trailing spaces
    return text
def get_answer(user_question):
    Questions=faqs.keys()
    vectoriser=TfidfVectorizer()
    all_question=list(Questions)+[preprocess(user_question)]
    vector=vectoriser.fit_transform(all_question) #converts all questions into numbers
    similarity=cosine_similarity(vector[-1],vector[:-1]) #compares user question with all faqs questions
    index=similarity.argmax() #finds the index of the most similar question
    matched_question=list(Questions)[index] #gets the matched question using the index
    answer=faqs[matched_question] #retrieves the answer from the faqs dictionary
    return answer
def send_message():
    user_question=user_input.get()
    user_input.delete(0,tk.END)
    chat_box.config(state="normal")
    chat_box.insert(tk.END,"You: "+user_question+"\n")
    chat_box.insert(tk.END,"Bot: "+get_answer(user_question)+"\n")
    chat_box.config(state="disabled")
window=tk.Tk()
window.title("FAQS Chatbot")
window.geometry("400x300")
chat_box=tk.Text(window,height=15,width=50,state="disabled")
chat_box.pack()
user_input=tk.Entry(window,width=40)
user_input.pack()
send_button=tk.Button(window,text="Send",command=send_message)
send_button.pack()


    
window.mainloop()








