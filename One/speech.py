speech = input("Speech:")
list = speech.split()
if "hello" == list[0][0:5].lower():
    print("$0")
elif "h" == list[0][0].lower():
    print("$20")
else:
    print("$100")
