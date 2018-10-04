# String

s = "I am a string."
print(type(s))

# Boolean

yes = True
print(type(yes))

no = False

print(type(no))

# Lit  -- ordered and changeable

alpha_list = ["a", "b", "c"]
print(type(alpha_list))
print(type(alpha_list[0]))	#prints the type of the 0'th element of the list!
alpha_list.append("d")
print(alpha_list)

# Tuple -- ordered and unchangeable

alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can;t add eements to tuples!")
print(alpha_tuple)
