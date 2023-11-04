"""
Question 2
The groups_per_user function receives a dictionary, 
which contains group names with the list of users. 
Users can belong to multiple groups. 
Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
"""

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for users, group in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
				if user in user_groups:
					user_groups[users].append(group)
				else:
					user_groups[users] = group
	return (user_groups)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary



print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))