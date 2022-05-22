import os
import pandas as pd
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import time
import codecs
from playsound import playsound

# import vlc
# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS

  
def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language,lang_check=True, slow=True)
    myobj.save(filename)
    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('Railway Station ! Samta Express ! Train Announcement.mp3')
 
    # 1 - Yatriyon kripya dhyan dijiye
    start =0
    finish =5500
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")
    # 2 - train no.
    # 3-from city
    
    # 4 -to city

    # 5-train name

    # 6 thodi der me platform number
    start=11000
    finish=13000
    audioProcessed = audio[start:finish]
    audioProcessed.export("6_hindi.mp3", format="mp3")
    
    # 7 platform no.

    # 8 par arhi hai
    start =13500
    finish =15000
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():#iterrows is a function in ffmpeg
        # 3 - train no.
        textToSpeech(item['Train no.'], '2_hindi.mp3')

        # 4 -from city 
        textToSpeech(item['From'], '3_hindi.mp3')

        # 6 - to city
        textToSpeech(item['To'], '4_hindi.mp3')

        # 8 - train name
        textToSpeech(item['Train'], '5_hindi.mp3')

        # 10 -platform no.
        textToSpeech(item['Platform'], '7_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,9)]

        announcement = mergeAudios(audios)
        play(announcement)#to play one by one after merging
        # time.sleep(2)
        # play(announcement)
        announcement.export(f"announcement_{item['Train no.']}_{index+1}.mp3", format="mp3")

        


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("train details.xlsx")
    fname='generalawareness.txt'   
    var=open(fname)
    with codecs.open(fname, encoding='utf-8') as f:
        tixt=f.read()
    obj=gTTS(text=tixt,lang='en',lang_check=True,slow=False)#slow=false for speeding up of audio
    obj.save("speech.mp3")
    os.system("speech.mp3")#to open audio file automaticallytld="com"
    time.sleep(45)
    fname1='delayed trains.txt'   
    var=open(fname1)
    with codecs.open(fname1, encoding='utf-8') as f:
        txt=f.read()
    obj=gTTS(text=txt,lang='en',lang_check=True,slow=False)#slow=false for speeding up of audio
    obj.save("speech1.mp3")
    os.system("speech1.mp3")