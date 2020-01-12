# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations You’ll have to think of
# someone else to invite
# •	 Start with your program from Exercise 3-4 Add a print statement at the
# end of your program stating the name of the guest who can’t make it
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting
# •	 Print a second set of invitation messages, one for each person who is still
# in your list


guest = ["barrack obama", "nelson mandela", "lebron james", "valentino rossi"]

msg_1 = ("Hi " + guest[0].title() + ". We are happy to have you attend our event today.")
print("\n" + msg_1)

msg_2 = ("Make sure that " + guest[2].title() + " and " + guest[1].title() + " are feeling comfortable.")
print("\n" + msg_2)

msg_3 = (guest[3] + " requested for some water." )
print("\n" + msg_3)

# Identified unavailable guest
unavailable = guest.pop(1)
print("\n" + unavailable.title() + " can't make it for today's event.")

# Replaced unavailable
guest[1] = "post malone"

print("\n" + unavailable.title() + " has now been replaced by " + guest[1].title())

# Second Set of invitations
msg_1 = ("Hi " + guest[0].title() + ". We are happy to have you attend our event today.")
print("\n" + msg_1)

msg_2 = ("Make sure that " + guest[2].title() + " and " + guest[1].title() + " are feeling comfortable.")
print("\n" + msg_2)

guest.insert(3, "Michael jackson")

msg_3 = (guest[3] + " requested for some water." )
print("\n" + msg_3)
