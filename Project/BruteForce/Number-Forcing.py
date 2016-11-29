import itertools

number_generator = ("".join(nums) for nums in itertools.permutations("0123456789", 4))
for n in number_generator
    print n
