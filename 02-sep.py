class Music:
    Music_platform="spotify"      #-----class varibles/static variables-------
    default_volume="50"

    def __init__(self,song_name,artist,duration):            #------------Instance variables------------
        self.song_name=song_name
        self.artist=artist
        self.duration=duration

    def play(self):
        print("song_name:",self.song_name,"Artist:",self.artist,"Duration:",self.duration)     #-----------Instance  method--------------
    @classmethod
    def change_Music_platform(cls,gaana):                #-----class method-----------
        cls.Music_platform=gaana
    @staticmethod
    def welcome_message():                               #--------static method------------
        print("Welcome to music player! Enjoy your song.........")

m1=Music("shiv dhun","Pandit Jasraj",10.36)
m1.welcome_message()                 #instance  can access staticmethod
m1.play()
# Music.play()                       #  cannot call instance method by class name
Music.play(m1)                       # instance method can be called by class if we pass object
m1.change_Music_platform("gaana")    #object can access class method   #Changes the class variable for ALL objects because class variables are shared
m2=Music("Believer","Imagine Dragons",4.0)
m2.play()
m3=Music("Blinding Lights","The weeeknd",3.5)
m3.play()
m4=Music("shape of you","Ed sheeran",4.2)
m4.play()
print("Songname:",m3.song_name)    #can access instance variable by object
print(Music.default_volume)       #can access class variable by class name
print("Artist:",m3.artist) 
print("Music_platform:",m3.Music_platform)
m2.Music_platform="spotify"          # creates an instance variable for m2 only
print(m2.Music_platform)
print("Duration:",m3.duration)
# print(Music.song_name)         #cannnot access instance variable by class name





