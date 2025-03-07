bible = input("What is the first book in the Bible? \n a) Genesis\n b) Exodus \n c) Numbers\n d) Leviticus \n>> ")

bible_list_correct = ["genesis", "a", "a)", "a) genesis"]
bible_list_incorrect = ["exodus", "numbers", "leviticus", "b", "c", "d", "b) exodus", "c) numbers", "d) leviticus"]

if bible.lower().strip() in bible_list_correct:
     print("That is correct")

elif bible.lower().strip() in bible_list_incorrect:
     print("That is incorrect")

else:
     print("That is a invalid answer")