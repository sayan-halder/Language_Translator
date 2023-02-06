import tkinter as tk
from tkinter import messagebox
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

root = tk.Tk()

root.geometry("400x400")

v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()

lang = {'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az',
        'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca',
        'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (simplified)': 'zh-cn', 'Chinese (traditional)': 'zh-tw',
        'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en',
        'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy',
        'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian creole': 'ht',
        'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu',
        'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja',
        'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish (kurmanji)': 'ku',
        'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb',
        'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi',
        'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no',
        'Odia': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa',
        'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st',
        'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so',
        'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta',
        'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz',
        'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}

def language():
    fl = clicked1.get()
    tl = clicked2.get()

    # Creating Recogniser() class object
    recog1 = spr.Recognizer()

    # Creating microphone instance
    mc = spr.Microphone()	

    # Translator method for translation
    translator = Translator()

    # short form of english in which you will speak
    from_lang = lang[fl]

    # In which we want to convert, short form of hindi
    to_lang = lang[tl]
        
    #print(from_lang)print(to_lang)

    with mc as source:
        print("Speak a stentence...")
        v1.set("Speak a stentence...")
        root.update()

        recog1.adjust_for_ambient_noise(source, duration=0.2)
                    
        # Storing the speech into audio variable
        audio = recog1.listen(source)
                    
        # Using recognize.google() method to convert audio into text
        get_sentence = recog1.recognize_google(audio)

        # Using try and except block to improve its efficiency.
        try:
            # Printing Speech which need to be translated.
            print("Speech to be Translated: "+get_sentence)
            v2.set(str(get_sentence))
            root.update()

            # Using translate() method which requires three arguments, 1st the sentence which
            # needs to be translated 2nd source language and 3rd to which we need to translate in
            text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
                            
            # Storing the translated text in text variable
            text = text_to_translate.text

            # Printing translated speech.
            print("Translated Speech: "+text)
            v3.set(str(text))
            root.update()

            # Using Google-Text-to-Speech ie, gTTS() method to speak the translated text into the
            # destination language which is stored in to_lang.
            # Also, we have given 3rd argument as False because by default it speaks very slowly
            speak = gTTS(text=text, lang="en", slow= False)

            # Using save() method to save the translated speech in capture_voice.mp3
            speak.save("speech.mp3")		

            playsound("speech.mp3")

            messagebox.showinfo("showinfo", "Conversion Done!!!!!!!!")

            # Here we are using except block for UnknownValue and Request Error and printing the same to
            # provide better service to the user.
        except spr.UnknownValueError:
            messagebox.showerror("showerror", "Unable to understand the Input")
            #print("Unable to understand the Input")
                            
        except spr.RequestError as e:
            messagebox.showerror("showerror", "Unable to provide Required Output".format(e))
            #print("Unable to provide Required Output".format(e))

Label1 = tk.Label(root, text ='Language From: ').place(relx = 0.05, rely = 0.05)

Label2 = tk.Label(root, text ='Language To: ').place(relx = 0.05, rely = 0.15)

options = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian',
           'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)',
           'Chinese (traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto',
           'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek',
           'Gujarati', 'Haitian creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian',
           'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh',
           'Khmer', 'Korean', 'Kurdish (kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',
           'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi',
           'Mongolian', 'Myanmar (burmese)', 'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish',
           'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots gaelic', 'Serbian', 'Sesotho',
           'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili',
           'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek',
           'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']

clicked1 = tk.StringVar()
clicked1.set("English")

clicked2 = tk.StringVar()
clicked2.set("English")
  
drop1 = tk.OptionMenu(root, clicked1, *options).place(relx = 0.3, rely = 0.04)

drop2 = tk.OptionMenu(root, clicked2, *options).place(relx = 0.3, rely = 0.14)

Label3 = tk.Label(root, textvariable = v1).place(relx = 0.1, rely = 0.36)

Label4 = tk.Label(root, textvariable = v2).place(relx = 0.1, rely = 0.46)

Label5 = tk.Label(root, textvariable = v3).place(relx = 0.1, rely = 0.56)

button = tk.Button(root, text = "Convert", command = language).place(relx = 0.2, rely = 0.26)

root.mainloop()
