from ast import main
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr
import pyttsx3
#import os
#import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
# print(voices[0].id)     #voice of male 
# print(voices[1].id)     #voice of female 
engine.setProperty('voice' , voices[1].id)

# -------------------------Function to let your device speak-------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        print("                                          Good morning Sir")
    elif hour >=12 and hour<18:
        print("                                          Good AfterNoon Sir")
    else:
        print("                                          Good Evening Sir")
    print("\n")
    print("                       I am PIEAS Chatbot Sir! Please tell me how may i help you")

def takeCommand():
    print("\n")
    query = input("user:")
    return query

def Command():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-in")
        #print(f"User said: {query}\n")  #User query will be printed.
    except Exception as err:
        # print(err)
        print("Say that again...!")
        return "None"
    # speak(query)
    return query


if __name__ == "__main__":
    print("\n")
    print("\n")
    print("\n")
    print("              ********************************************************************************")
    print("              -------------------------PIEAS ADMISSION FAQ CHATBOT----------------------------")
    print("              ********************************************************************************")
    print("\n")
    wishMe()
    print("                           This is text to text and Speech to speech Chatbot")
    print("\n")
    print("Enter 1 if you want text to text chat")
    print("Enter 0 for speech to speech chat")
    n = int(input("Enter your Choice: "))
    
    if n==1:
        while True:
            query = takeCommand().lower()


            if 'famous' in query:
                print("Bot : PIEAS offers on-campus residence to its students as there are numerous benefits to living on campus including convenience, opportunities to develop life-long friendships, and to live in an environment that fosters the educational and personal growth of students.")

            elif 'good university' in query:
                print("Bot : PIEAS faculty is highly qualified, over 90 percent of the faculty members are PhD. PIEAS is a research intensive university, In faculty strength, it ranks number one in Pakistan, and 15th in Asia. Its number of publications per faculty member is the highest in Pakistan, 67th in Asia")
            
            elif 'good score for pieas entry test' in query:
                print("Bot : A minimum score of 2000 is required. The PIEAS institutional code to receive SAT scores is 7272.")
            
            elif 'pieas stands for' in query:
                print("Bot : PIEAS is an abbreviation of Pakistan Institute of Engineering and Applied Sciences.")
                    
            elif 'ranking' in query:
                print("Bot : It is ranked 390 in qs world university rankings 2023.")

            elif 'apply for admission in pieas' in query:
                print("Bot : Admissions are announced in April/May every year. Admissions are announced through advertisements in renowned national NEWS papers of Pakistan. Announcement for admission is also highlighted on PIEAS website.")
            
            elif 'procedure for application' in query:
                print("Bot : A candidate seeking admission in PIEAS has to apply online through a link on PIEAS website.")
                
            elif 'registration fee' in query:
                print("Bot : 2000 PKR.")
                
            elif 'scholarship'  in query:
                print("Bot : PIEAS provide need based financial support in the form of tuition fee waiver subject to satisfactory performance..")
                    
            elif 'apply for more than one program' in query:
                print("Bot : Yes. He /She can make a choice between Electrical Engg., Mechanical Engg., Chemical Engg., Metallurgy and Materials Engg., Computer and Information Sciences or Physics.")
                
            elif 'change test center' in query:
                print("Bot : No.")
                
            elif 'foreigner' in query:
                print("Bot : Foreign students seeking admissions to this Institute are required to submit their applications through the Ministries of Foreign Affairs / Education, Government of Pakistan.")
                
            elif 'equivalence certificate' in query:
                print("Bot : Yes. It is necessary.")
                
            elif 'age limit' in query:
                print("Bot : There is no age limit for regular fee paying students.")
                
            elif 'refundable' in query:
                print("Bot : No. Admission processing fee once deposited cannot be refunded.")
                
            elif 'queries' in query:
                print("Bot :You can contact at Director Academics, PIEAS. email = admissions@pieas.edu.pk")
                
            elif 'list' in query:
                print("Bot : A list of successful candidates is made available on our website after about 4-6 weeks of the admission written test.")
                
            elif 'change department' in query:
                print("Bot : Yes. You can change once, provided you are eligible for the new discipline and a vacant seat is available.")
                
            elif 'duration' in query:
                print("Bot : The normal duration of bachelors degree at PIEAS is 4(four) years and Masters Degree is 2(two) years.")
                
            elif 'dae' in query:
                print("Bot : Yes, DAE holders with 60% marks both in Matric and DAE are eligible to apply for admission. They must have studied Physics, Chemistry and Mathematics for admission to BS engineering programs and Physics & Mathematics as major subject for admission to BS Computer & Information Sciences program and Physics.")
                
            elif 'location' in query:
                print("Bot : PIEAS is located in Nilore which is a suburb town 26km from Islamabad.")
                
            elif 'shuttle service' in query:
                print("Bot : PIEAS has dedicated bus shuttle service for its students residing in Rawalpindi and Islamabad.")
                
            elif 'bus' in query:
                print("Bot : PIEAS has dedicated bus shuttle service for its students residing in Rawalpindi and Islamabad.")
                
            elif 'sat' in query:
                print("Bot : PIEAS has reserved some seats for admission in BS programs through SAT scores")
                
            elif 'freeze semester' in query:
                print("Bot : Expect first semester All semesters can be freezed.")
                
            elif 'deposit fee challan' in query:
                print("Bot : You Can deposit fee challan in any branch of ASKARI Bank")
                
            elif 'spring admission' in query:
                print("Bot : No")
                
            elif 'domicile' in query:
                print("Bot : Yes it necessary")
                
            elif 'best program' in query:
                print("Bot : The Best Program Offered in PIEAS is CIS")

            elif 'wikipedia' in query:
                print('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                print("According to Wikipedia")
                print(results)

            elif 'pieas website' in query:
                webbrowser.open('http://www.pieas.edu.pk/')
                
            elif 'sample papers' in query:
                webbrowser.open('https://www.paklearningspot.com/2022/03/pieas-university-entry-test.html#:~:text=The%20test%20will%20have%20three,30%20MCQs%20from%20the%20syllabus')
                
            elif 'syllabus' in query:
                webbrowser.open('https://www.paklearningspot.com/2022/03/pieas-university-entry-test.html#:~:text=The%20test%20will%20have%20three,30%20MCQs%20from%20the%20syllabus')
                
            elif 'migration policy' in query:
                webbrowser.open('http://admissions.pieas.edu.pk/Academic_Rules/Academic_rules_for_BS_Aug2017.pdf')
                
            elif 'admission schedule' in query:
                webbrowser.open('http://admissions.pieas.edu.pk/Admissions/schedule.html')
                
            elif 'fee structure' in query:
                webbrowser.open('http://admissions.pieas.edu.pk/Academic_Rules/fee_structure.html')
                
            elif 'information' in query:
                webbrowser.open('http://www.pieas.edu.pk/departments.cshtml')
            
            elif 'exit' in query:
                break
            
            else:
                print("Coudn't understand. Try again")
    
    elif n==0:
        while True:
            query = Command().lower()

            if 'famous' in query:
                speak("PIEAS offers on-campus residence to its students as there are numerous benefits to living on campus including convenience, opportunities to develop life-long friendships, and to live in an environment that fosters the educational and personal growth of students.")

            elif 'good university' in query:
                speak("PIEAS faculty is highly qualified, over 90 percent of the faculty members are PhD. PIEAS is a research intensive university, In faculty strength, it ranks number one in Pakistan, and 15th in Asia. Its number of publications per faculty member is the highest in Pakistan, 67th in Asia")
            
            elif 'good score for pieas entry test' in query:
                speak("A minimum score of 2000 is required. The PIEAS institutional code to receive SAT scores is 7272.")
            
            elif 'pieas stands for' in query:
                speak("PIEAS is an abbreviation of Pakistan Institute of Engineering and Applied Sciences.")
                    
            elif 'ranking' in query:
                speak("It is ranked 390 in qs world university rankings 2023.")

            elif 'apply for admission in pieas' in query:
                speak("Admissions are announced in April/May every year. Admissions are announced through advertisements in renowned national NEWS papers of Pakistan. Announcement for admission is also highlighted on PIEAS website.")
            
            elif 'procedure for application' in query:
                speak("A candidate seeking admission in PIEAS has to apply online through a link on PIEAS website.")
                
            elif 'registration fee' in query:
                speak("2000 PKR.")
                
            elif 'scholarship'  in query:
                speak("PIEAS provide need based financial support in the form of tuition fee waiver subject to satisfactory performance..")
                    
            elif 'apply for more than one program' in query:
                speak("Yes. He /She can make a choice between Electrical Engg., Mechanical Engg., Chemical Engg., Metallurgy and Materials Engg., Computer and Information Sciences or Physics.")
                
            elif 'change test center' in query:
                speak("No.")
                
            elif 'foreigner' in query:
                speak("Foreign students seeking admissions to this Institute are required to submit their applications through the Ministries of Foreign Affairs / Education, Government of Pakistan.")
                
            elif 'equivalence certificate' in query:
                speak("Yes. It is necessary.")
                
            elif 'age limit' in query:
                speak("There is no age limit for regular fee paying students.")
                
            elif 'refundable' in query:
                speak("No. Admission processing fee once deposited cannot be refunded.")
                
            elif 'queries' in query:
                speak("You can contact at Director Academics, PIEAS. email = admissions@pieas.edu.pk")
                
            elif 'list' in query:
                speak("A list of successful candidates is made available on our website after about 4-6 weeks of the admission written test.")
                
            elif 'change department' in query:
                speak("Yes. You can change once, provided you are eligible for the new discipline and a vacant seat is available.")
                
            elif 'duration' in query:
                speak("The normal duration of bachelors degree at PIEAS is 4(four) years and Masters Degree is 2(two) years.")
                
            elif 'dae' in query:
                speak("Yes, DAE holders with 60% marks both in Matric and DAE are eligible to apply for admission. They must have studied Physics, Chemistry and Mathematics for admission to BS engineering programs and Physics & Mathematics as major subject for admission to BS Computer & Information Sciences program and Physics.")
                
            elif 'location' in query:
                speak("PIEAS is located in Nilore which is a suburb town 26km from Islamabad.")
                
            elif 'shuttle service' in query:
                speak("PIEAS has dedicated bus shuttle service for its students residing in Rawalpindi and Islamabad.")
                
            elif 'bus' in query:
                speak("PIEAS has dedicated bus shuttle service for its students residing in Rawalpindi and Islamabad.")
                
            elif 'sat' in query:
                speak("PIEAS has reserved some seats for admission in BS programs through SAT scores")
                
            elif 'freeze semester' in query:
                speak("Expect first semester All semesters can be freezed.")
                
            elif 'deposit fee challan' in query:
                speak("You Can deposit fee challan in any branch of ASKARI Bank")
                
            elif 'spring admission' in query:
                speak("No. PIEAS do not offer spring admissions")
                
            elif 'domicile' in query:
                speak("Yes it necessary")
                
            elif 'best program' in query:
                speak("The Best Program Offered in PIEAS is CIS")

            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak(results)
                speak("According to Wikipedia")
                speak(results)

            elif 'pieas website' in query:
                webbrowser.open('http://www.pieas.edu.pk/')
                
            elif 'sample papers' in query:
                webbrowser.open('https://www.paklearningspot.com/2022/03/pieas-university-entry-test.html#:~:text=The%20test%20will%20have%20three,30%20MCQs%20from%20the%20syllabus')
                
            elif 'syllabus' in query:
                webbrowser.open('https://www.paklearningspot.com/2022/03/pieas-university-entry-test.html#:~:text=The%20test%20will%20have%20three,30%20MCQs%20from%20the%20syllabus')
                
            elif 'migration policy' in query:
                webbrowser.open('http://admissions.pieas.edu.pk/Academic_Rules/Academic_rules_for_BS_Aug2017.pdf')
                
            elif 'admission schedule' in query:
                webbrowser.open('http://admissions.pieas.edu.pk/Admissions/schedule.html')
                
            elif 'fee structure' in query:
                webbrowser.open('http://admissions.pieas.edu.pk/Academic_Rules/fee_structure.html')
                
            elif 'information' in query:
                webbrowser.open('http://www.pieas.edu.pk/departments.cshtml')

            elif 'exit' in query:
                break

            #else:
                #speak("Couldn't unerstand please say again")

    print("Thankyouu. Have a Nice Day")




        
        