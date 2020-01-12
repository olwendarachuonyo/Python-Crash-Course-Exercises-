# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner Then use your list to print a message to each person, inviting
# them to dinner
print("\n")
guest = ["barrack obama", "nelson mandela", "lebron james", "valentino rossi"]

msg_1 = ("Hi " + guest[0].title() + ". We are happy to have you attend our event today")
print(msg_1)
print("\n")
msg_2 = ("Make sure that " + guest[2].title() + " and " + guest[1].title() + " are feeling comfortable.")
print(msg_2)
print("\n")
msg_3 = (guest[3] + " resquested for some water" )
print(msg_3)
print("\n")
