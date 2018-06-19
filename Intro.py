print("Welcome to Madlibs")


pluralnoun = raw_input("please provide a plural noun:")
noun1 = raw_input("please provide a noun:")
noun2 = raw_input("please provide a noun:")
song = raw_input("please provide the title of a song")
verb = raw_input("please provide a verb:")
madlibs = ("Learning to drive is a tricky process.  There are a few
1. Keep two %s on the steering wheel at all times
2 . Step on the %s to speed up and the %s to slow down
3. Your parents will just LOVE it if you play $ on the radio
4. Make sure to honk your horn when you see %s on a street sign.")

print(madlibs %(plural_noun,noun1,noun2,song,verb))