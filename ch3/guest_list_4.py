# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests
# •	 Start with your program from Exercise 3-6 Add a new line that prints a
# message saying that you can invite only two people for dinner
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited
# •	 Use del to remove the last two names from your list, so you have an empty
# list Print your list to make sure you actually have an empty list at the end
# of your program

guest = ["barrack obama", "nelson mandela", "lebron james", "valentino rossi"]

msg_1 = ("Hi " + guest[0].title() + ". We are happy to have you attend our event today.")
print("\n" + msg_1)

msg_2 = ("Make sure that " + guest[2].title() + " and " + guest[1].title() + " are feeling comfortable.")
print("\n" + msg_2)

msg_3 = (guest[3] + " requested for some water." )
print("\n" + msg_3)

print("\nGood news people! We found a bigger table to accommodate more guests!")
guest.insert(0, "michael jackson")
# print(guest)
guest.insert(2, "post malone")
# print(guest)
guest.append('jay leno')
# print(guest)

print("\nFor a total of six guests. We have now welcomed on-board; ")
print("\n" + guest[0].title()+", " + guest[2].title()+" and " + guest[6].title())
print("\nWe are glad to have them along.")
print(guest)

# Can only invite two people to the dinner now
print("\n\nHey guys, sorry, we only have space for two guests now.")
popped_guest = guest.pop()
print("\nSorry " + popped_guest.title() + ". Come back next time.")
popped_guest = guest.pop()
print("\nSorry " + popped_guest.title() + ". Come back next time.")
popped_guest = guest.pop()
print("\nSorry " + popped_guest.title() + ". Come back next time.")
popped_guest = guest.pop()
print("\nSorry " + popped_guest.title() + ". Come back next time.")
popped_guest = guest.pop()
print("\n")

print("Worry not " + guest[0].title() + ". You're still invited.")
print("Worry not " + guest[1].title() + ". You're still invited.")
print(guest)
print(popped_guest)

del guest[0:2]
# del guest[0]
print(guest)
