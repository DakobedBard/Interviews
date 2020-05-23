


def distributeCandies(candies, num_people):

    candy_array = [0] * num_people
    n_loops = 0
    i = 0
    while candies > 0:
        n_candies =(n_loops*num_people)+1+(i % num_people)
        if n_candies > candies:
            candy_array[i % num_people] += candies
            break
        else:
            candy_array[i % num_people] += n_candies
            candies -= n_candies
            print(candy_array)
            i +=1
        if i % num_people == 0:
            n_loops +=1
    return candy_array

candies = 60
num_people = 4
print("the distribution of candies w/ {} candies and {} people is {}".format(candies, num_people, distributeCandies(candies, num_people)))