iScore = int(input("What is the score?: "))
#
# if iScore == 100:
#     print(f"""You have passed
# You have a perfect Score""")
# elif iScore >= 90:
#     print("You have passed")
# else:
#     print("You have failed")

if iScore >= 100:
    print("Pass")
    if iScore == 100:
        print("Perfect score")
else:
    print("Retake")
