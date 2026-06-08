# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 1
# Wordle
# last revised 5/24/25
#
# In this code, the computer guesses randomly.  Not great.
# Can you implement our better algorithm by rewriting guessWord()?
#
# Note that this demo uses only the 18 words from Chapter One. The idea
# is to keep things simple so that we can really see what happens at
# every step. Once you have revised the code, however, feel free to
# replace the wordList with something much longer.

import random

# FUNCTIONS

def loadWordList(filename):
    wordList = []

    wordFile = open(filename)
    for line in wordFile:
        word = line.strip()
        if len(word) == 5:
            wordList.append(word)
    wordFile.close()

    return wordList

def scoreGuess(guess, hiddenWord):
    # returns Y for yellow letters, G for green, blank otherwise
    # when you code, you will use this information to pick your next guess

    hiddenLettersUsed = [False, False, False, False, False]
    guessLettersUsed = [False, False, False, False, False]
    colors = ["_", "_", "_", "_", "_"]

    # go through the guess and make any matches green
    for letter in range(5):
        if guess[letter] == hiddenWord[letter]:
            hiddenLettersUsed[letter] = True
            guessLettersUsed[letter] = True
            colors[letter] = "G"

    # then go through the guess and make any remaining matches yellow
    for letter in range(5):
        if guessLettersUsed[letter] == False:
            for possibleMatch in range(5):
                if guessLettersUsed[letter] == False and hiddenWord[possibleMatch] == guess[letter] and \
                        hiddenLettersUsed[possibleMatch] == False:
                    guessLettersUsed[letter] = True
                    hiddenLettersUsed[possibleMatch] = True
                    colors[letter] = "Y"

    return (colors)


def hideWord(availableList):
    # this function randomly chooses one word from the list

    randomChoice = random.randint(0, len(availableList) - 1)
    chosenWord = availableList[randomChoice]

    return chosenWord


def removeDuds(availableList, previousOutcome, previousGuess):
    # remove words that could not have given us the previousOutcome
    # also remove the word that was guessed unsuccessfully

    newList = []

    for word in availableList:
        if scoreGuess(previousGuess, word) == previousOutcome:
            if previousGuess != word:
                newList.append(word)

    return newList


def guessWord_mm(availableList, wordList):
    # we will attempt an algorithm that uses worse case scenario first, we will then move onto 
    best_word = None
    abs_best_worst_case = float("INF")
    if len(availableList) == 1:
        return availableList[0]
    for w in availableList: #Gives every word possible that is left    
        # i want to build a dictionary giving me the counts for every outcome
        outcome_counts = {} 

        for w2 in availableList:
            if w != w2:
                outcome = tuple(scoreGuess(w, w2))
                if outcome not in outcome_counts:
                    outcome_counts[outcome] = 1
                else:
                    outcome_counts[outcome] += 1
        worst_case = max(outcome_counts.values())
        if worst_case < abs_best_worst_case:
            abs_best_worst_case = worst_case
            best_word = w
    return best_word
def guessWord_avg(availableList, wordList):
    best_word = None
    abs_best_avg = float("INF")
    if len(availableList) == 1:
        return availableList[0]
    for w in availableList: #Gives every word possible that is left    
        # i want to build a dictionary giving me the counts for every outcome
        outcome_counts = {} 

        for w2 in availableList:
            if w != w2:
                outcome = tuple(scoreGuess(w, w2))
                if outcome not in outcome_counts:
                    outcome_counts[outcome] = 1
                else:
                    outcome_counts[outcome] += 1
        # i need to calculate the weighted average from the outcome counts dictionary
        # for example if we have 600 total words, and the worst case is 18 words remaining, we would do 18/600 * 18, also seen as probability * remaining words : 
        # remaining_words/total_words * remaining_words
        avg_remaining = sum([count * count for count in outcome_counts.values()]) / len(availableList)
        if avg_remaining < abs_best_avg:
            abs_best_avg = avg_remaining
            best_word = w
            
    return best_word

        





# ############
# main program
# ############

# make a list of all the words the computer knows
wordList = ["adept", "after", "agent", "avert", "cater", "eaten", "eater", "extra", "hater", "taken", "taker", "water",
            "great", "treat", "wheat", "taper", "tread", "tweak"]
wordList = random.sample(loadWordList("wordle_words.txt"), 1000)

# we want to run 20 word rollouts for each algorithm (minimax vs average)
num_rollouts_mm = 0
minimax_method_total = 0
avg_method_total = 0
while num_rollouts_mm < 20:

    # make a separate list that will be updated to keep track of which words might still be the hidden word
    availableList = []
    for word in range(len(wordList)):
        availableList.append(wordList[word])

    # initialize other variables
    hiddenWord = hideWord(availableList)
    guess = ""
    counter = 0

    print("")
    print("MINIMAX: The hidden word is %s." % hiddenWord)
    print("")
    
    # minimax method
    while guess != hiddenWord:
        guess = guessWord_mm(availableList, wordList)
        counter = counter + 1
        print("Computer guesses: ", guess)
        outcome = scoreGuess(guess, hiddenWord)
        print(outcome)
        availableList = removeDuds(availableList, outcome, guess)
        print("  ", len(availableList), "words remaining.")

        # failsafe to stop infinite loops
        if counter > len(wordList):
            print("Something has gone wrong - try again!")
            break
    print("")
    print("The computer needed %d guesses." % counter)
    minimax_method_total += counter
    num_rollouts_mm += 1
    print(num_rollouts_mm)

num_rollouts_avg = 0
while num_rollouts_avg < 20:

    # make a separate list that will be updated to keep track of which words might still be the hidden word
    availableList = []
    for word in range(len(wordList)):
        availableList.append(wordList[word])

    # initialize other variables
    hiddenWord = hideWord(availableList)
    guess = ""
    counter = 0

    print("")
    print("AVERAGES: The hidden word is %s." % hiddenWord)
    print("")
    # averages method

    avg_counter = 0
    while guess != hiddenWord:
        guess = guessWord_avg(availableList, wordList)
        avg_counter += 1
        print("Computer guesses: ", guess)
        outcome = scoreGuess(guess, hiddenWord)
        print(outcome)
        availableList = removeDuds(availableList, outcome, guess)
        print("  ", len(availableList), "words remaining.")

        # failsafe to stop infinite loops
        if avg_counter > len(wordList):
            print("Something has gone wrong - try again!")
            break
    print("The computer needed %d guesses." % avg_counter)
    avg_method_total += avg_counter


    num_rollouts_avg += 1
print(f"Minimax average: {minimax_method_total/20}")
print(f"Average method average: {avg_method_total/20}")
