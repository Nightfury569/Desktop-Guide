import pyttsx3,wikipedia,webbrowser,os,datetime,cv2,random,turtle,time
#from googletrans import LANGUAGES,Translator

import speech_recognition as sr
r = sr.Recognizer()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Listen():
  with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source)
    print("Listening..")
    #r.energy_threshold = 400
    audio = r.listen(source)
    try:
          text = r.recognize_google(audio)
          #print('command ='+ text)
          return text
    except :
        return
c=1
speak("I am Kendra,your assistant. how may I help you? ")
while c==1:
 p = Listen()
 if p is not None:
     p = p.lower()

 print(p)

 if p is None:
    speak("you did not say anything")
# Folders
 elif p[0:11] == "open folder":
    #speak("Yes next ?")
    #l = Listen()
    l = p[12:len(p)]
    try:
        os.startfile('C:\\Users\\prant\\'+l)
    except:
      for i in range(5, len(p)):
        if p[11] == " " and l[0].isupper() == False:
          l[0].upper()
        os.startfile('C:\\Users\\prant\\'+l)

 elif p == "drive c" or p=="drive see" or p=="drive sea" :
    speak("Next")
    try:
      l1 = Listen()
      print(l1)
      if l1[0:11] == "open folder":
        l = l1[12:len(l1)]
        try:
          os.startfile('C:\\'+l)
        except:
          try:
           for i in range(5, len(p)):
             if p[11] == " " and l[0].isupper() == False:
               l[0].upper()
           os.startfile('C:\\'+l)
          except :
            speak("Not found")
      elif l1=="open":
         os.startfile('C:\\')
    except:
          print("I didn't get it")

 elif p == "drive d" or p=="drive dee" or p=="drive De" :
    speak("Next")
    try:
      l1 = Listen()
      print(l1)
      if l1[0:11] == "open folder":
        l = l1[12:len(l1)]
        try:
          os.startfile('D:\\'+l)
        except:
         try:
           for i in range(5, len(p)):
              if p[11] == " " and l[0].isupper() == False:
               l[0].upper()
           os.startfile('D:\\'+l)
         except :
            speak("Not found")
      elif l1=="open":
         os.startfile('D:\\')
    except:
        print("I didn't get it")


#Date and time
 elif p== "what is the date":
    try:
        speak(datetime.date.today())
        print(datetime.date.today())
    except:
        speak("I didn't get it")

 elif p =="which day is today":
    try:
        speak("today is "+datetime.datetime.now().strftime("%A"))
    except:
        speak("I didn't get it")

 elif p== "what is the time now":
    try:
        speak("Now it is "+datetime.datetime.now().strftime("%H:%H:%S"))
    except:
        speak("I didn't get it")


#Google
 elif p == "open Google":
    try:
        webbrowser.open_new('https://google.com')
    except:
        speak("Sorry could not get it")

 elif p == "Google search":
    try:
        speak("What do you wanna search ?")
        g = Listen()
        webbrowser.open_new('https://google.com/search?q='+g)
    except:
        speak("Sorry could not get it")


#Wikipedia
 elif p[(len(p)-9):len(p)] == "Wikipedia":
    webbrowser.open_new('https://en.wikipedia.org/wiki/'+p[0:(len(p)-10)])
    results = wikipedia.summary(p,sentences=3)
    speak("According to wikipedia ")
    speak(results)

#read
 elif p[0:4]== "read":
   try:
    try:
        f= open('C:\\Users\\prant\\Desktop\\'+p[5:len(p)]+'.txt','r')
    except:
      for i in range (5,len(p)):
        if p[i-1]==" " and p[i].isupper() == False:
          p[i].upper()
      f= open('C:\\Users\\prant\\Desktop\\'+p[5:len(p)]+'.txt','r')

    data = f.read()
    speak(data)
    f.close()
   except:
     speak("Not found")

#Youtube
 elif p == "open YouTube":
    try:
        webbrowser.open_new('https://www.youtube.com')
    except:
        speak("I did not get that")

 elif p[0:14] == "search YouTube":
    try:
        webbrowser.open_new('https://www.youtube.com/results?search_query='+p[15:len(p)])
    except:
        speak("I did not get that")

#Email
 elif p=="open email":
    try:
        webbrowser.open_new('https://mail.google.com/mail/u/0/#inbox')
    except:
        speak("I did not get that")

 elif p[0:20]=="search email address":
    try:
        webbrowser.open_new('https://mail.google.com/mail/u/0/#search/'+p[21:len(p)])
    except:
        speak("I did not get that")

#ONA and Greeting to Guest
 elif p=="tell something about me":
    speak("you are Prantik Chongdar. You are a jadavpur university mechanical engineering student. You live in Howrah. You love football, watching movies, and eating.")

 elif p=="tell something about you":
    speak("I am kendra.I am a basic desktop assistant I was made by Prantik on 19th july,2020, the day was sunday.")

 elif p[0:4]=="greet":
    speak("greetings"+p[5:len(p)])


 elif p=="greet me":
    speak("greetings Prantik")

#wishing
 elif p=="wish me":
    speak("Welcome sir, I am kendra at your service. Wishing you a very bright day.")


#Play Recording:
 elif p=="play song":
  music_dir = 'C:\\Users\\prant\\Documents\\Sound recordings'
  c=0
  songs = os.listdir(music_dir)
  os.startfile(os.path.join(music_dir, songs[random.randrange(0,len(songs))]))

  #Facebook
 elif p == "open facebook":
   webbrowser.open_new('https://www.facebook.com/')

 elif p == "my facebook profile":
     webbrowser.open_new('https://www.facebook.com/prantik.chongdar.3')

 elif p[0:15]== "search facebook":
     webbrowser.open_new('https://www.facebook.com/search/top?q='+p[15:len(p)])



#webcam
 elif p=="open webcam":
    try:
     font = cv2.FONT_HERSHEY_COMPLEX
     fontScale = 1
     color = (0, 255, 0),
     thickness = 2

     video = cv2.VideoCapture(0)
     face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
     a = 1
     while True:
         a = a + 1

         check, frame = video.read()

         faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

         for x, y, w, h in faces:
             frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (230, 0, 200), 3)

             # putting text in the window
             frame = cv2.putText(frame, 'Face', (x, y), font, fontScale, (230, 0, 200), thickness)

         # print(check)

         cv2.imshow("Capture", frame)

         if cv2.waitKey(1) == ord('q'):
             break
     video.release()
     cv2.destroyAllWindows()
    except:
        speak("Not done")

# Stop Assistant
 elif p=="stop":
     speak("ok, goodbye")
     c=1
     exit(0)

# Translate
 #elif p[0:8]=="translate":
   #try:
     #t = Translator().translate(p[9:len(p)],src='en',dest='bn')
     #speak(t.text)
   #except:
       #speak("Sorry, could not do that")



 # Snake game
 elif p=="open snake game":
  speak("ok")
  c=0
  delay = 0.1

 # scores
  score = 0
  high_score = 0

 # set up th screen
  wn = turtle.Screen()

  wn.title("Snake game by Prantik")
  wn.bgcolor("grey")
  wn.setup(width=600, height=600)
  wn.tracer(0)  # tracer turns off the screen update

 # Snake head
  head = turtle.Turtle()
  head.speed(0)
  head.shape("square")
  head.color("blue")
  head.penup()
  head.goto(0, 0)
  head.direction = "stop"

 # Snake head
  food = turtle.Turtle()
  food.speed(0)
  food.shape("circle")
  food.color("red")
  food.penup()
  food.goto(0, 100)

  segments = []

 # Pen
  pen = turtle.Turtle()
  pen.speed(0)
  pen.shape("square")
  pen.color("black")
  pen.penup()
  pen.hideturtle()
  pen.goto(0, 270)
  pen.write(" Score = 0  High Score = 0", align="center", font=("Courier", 20, "bold"))


 # Functions
  def go_up():
     if head.direction != "down":
         head.direction = "up"


  def go_down():
     if head.direction != "up":
         head.direction = "down"


  def go_right():
     if head.direction != "left":
         head.direction = "right"


  def go_left():
     if head.direction != "right":
         head.direction = "left"


  def move():
     if head.direction == 'up':
         y = head.ycor()
         head.sety(y + 20)

     if head.direction == 'down':
         y = head.ycor()
         head.sety(y - 20)

     if head.direction == 'left':
         x = head.xcor()
         head.setx(x - 20)

     if head.direction == 'right':
         x = head.xcor()
         head.setx(x + 20)


 # Keyboard bindings
  wn.listen()
  wn.onkeypress(go_up, "Up")
  wn.onkeypress(go_down, "Down")
  wn.onkeypress(go_left, "Left")
  wn.onkeypress(go_right, "Right")

 # Main game loop
  while True:

     wn.update()

     # Check for collision with the border
     if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
         score = 0
         pen.clear()
         pen.write("Score = {}  High Score = {}".format(score, high_score), align="center",
                   font=("Courier", 20, "bold"))
         time.sleep(0.2)
         head.goto(0, 0)
         head.direction = "stop"

         # Hide the segments
         for segment in segments:
             segment.goto(1000, 1000)

         #  Clear the segments
         segments.clear()

     # Check for collision with the food
     if head.distance(food) < 20:
         # Move food to random spot
         x = random.randint(-290, 290)
         y = random.randint(-290, 290)
         food.goto(x, y)

         # Add snake segment
         new_segment = turtle.Turtle()
         new_segment.speed(0)
         new_segment.shape("square")
         new_segment.color("sky blue")
         new_segment.penup()
         segments.append(new_segment)

         # increase score
         score = score + 1
         if score > high_score:
             high_score = high_score + 1

         pen.clear()
         pen.write("Score = {}  High Score = {}".format(score, high_score), align="center",
                   font=("Courier", 20, "bold"))

     # Move the end segments first in reverse order
     for i in range(len(segments) - 1, 0, -1):
         x = segments[i - 1].xcor()
         y = segments[i - 1].ycor()
         segments[i].goto(x, y)

     # Move the zeroth segment
     if len(segments) > 0:
         x = head.xcor()
         y = head.ycor()
         segments[0].goto(x, y)

     move()

     # Check for collision between head and segments
     for segment in segments:
         if segment.distance(head) < 20:
             score = 0
             pen.clear()
             pen.write("Score = {}  High Score = {}".format(score, high_score), align="center",
                       font=("Courier", 20, "bold"))
             time.sleep(0.2)
             head.goto(0, 0)
             head.direction = "stop"

             # Hide the segments
             for segment in segments:
                 segment.goto(1000, 1000)

             #  Clear the segments
             segments.clear()

     time.sleep(delay)
  wn.mainloop()




 else:
    speak("Sorry could not recognize")
    c=1




