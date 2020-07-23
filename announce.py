import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway_announcement.mp3')

    # 1 - sound
    start = 0
    finish =1000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 Yatriyon kripya dhyan dijiye
    start = 13000
    finish =14000
    audioProcessed = audio[start:finish]
    audioProcessed.export("2_hindi.mp3", format="mp3")


    # 3 - train no.
    # 4-from city
    # 5 se
    start =18600
    finish = 18800
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 -to city

    # 7 - tak jane wali
    start = 19000
    finish = 20000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8-train name

    # 9 - thodi der me platform number
    start = 22000
    finish = 24500
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 platform no.

    # 11 par ayegi
    start = 25905
    finish = 26000
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():#iterrows is a function in ffmpeg
        # 3 - train no.
        textToSpeech(item['Train no.'], '3_hindi.mp3')

        # 4 -from city 
        textToSpeech(item['From'], '4_hindi.mp3')

        # 6 - to city
        textToSpeech(item['To'], '6_hindi.mp3')

        # 8 - train name
        textToSpeech(item['Train'], '8_hindi.mp3')

        # 10 -platform no.
        textToSpeech(item['Platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['Train no.']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("train details.xlsx")
    


