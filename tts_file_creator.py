from gtts import gTTS
print("Google TTS Generator")
print("Made by Raiden using gTTS")
tts = gTTS(input("Enter the text :"), lang=input("Enter the language (exemple : fr, en, es...) :"))
with open(input("Enter the file name :") + str(".mp3"), 'wb') as f:
    tts.write_to_fp(f)