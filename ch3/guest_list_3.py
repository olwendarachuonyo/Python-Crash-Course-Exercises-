# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available Think of three more guests to invite to dinner
# •	 Start with your program from Exercise 3-4 or Exercise 3-5 Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table
# •	 Use insert() to add one new guest to the beginning of your list
# •	 Use insert() to add one new guest to the middle of your list
# •	 Use append() to add one new guest to the end of your list
# •	 Print a new set of invitation messages, one for each person in your list

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
