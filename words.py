season = input("What is your favourite season: ")

season_list = ["summer", "winter", "autumn", "spring", "fall"]

if season.lower().strip() in season_list:
     print("That is a valid season")
else:
     print("That is not a valid season")
