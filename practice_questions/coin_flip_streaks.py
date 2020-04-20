# Coin Flip Streaks
# For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row

def coin_flip_streaks_counter(flip_number):
    import random

    # generate a list of flip results
    flip_results_list = []
    for i in range(flip_number):
        flip_results_list.append(random.choice(['h','t']))
    # print(flip_results_list)

    # find out if there is a streak of six heads or six tails
    flip_streak = 0
    for idx, item in enumerate(flip_results_list):
        if flip_results_list[idx+1:idx+6] == [item,item,item,item,item]:
            flip_streak += 1
    return "The number of a streak of 6 tails or 6 heads when a coin is flipped {} times is {}".format(flip_number, flip_streak)

print(coin_flip_streaks_counter(10))
print(coin_flip_streaks_counter(100))
print(coin_flip_streaks_counter(1000))
print(coin_flip_streaks_counter(10000))
print(coin_flip_streaks_counter(100000))
