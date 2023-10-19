# You have a basket of 30 eggs that you want to
# distribute equally among a group of 4 friends.
# However, you want to ensure that each friend
# receives the same number of eggs.
#
# Write a Python program to calculate and print
# the number of eggs each friend will receive,
# as well as the number of eggs left in the basket.

eggs = 50
friends = 5

eggs_per_friend = eggs // friends

eggs_left = eggs % friends

print("Each friend received", eggs_per_friend, "eggs.")
print(eggs_left, "eggs left in the basket.")

