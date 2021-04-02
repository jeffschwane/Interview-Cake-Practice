import random


def get_random(floor, ceiling):
    """Returns a random integer between floor and ceiling, inclusive"""
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    """Shuffles the input list in place"""
    
    end = len(the_list) - 1
    
    for i in range(0, end):
        i_rand = get_random(i, end)
        if i != i_rand:
            the_list[i], the_list[i_rand] = the_list[i_rand], the_list[i]
    

sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)