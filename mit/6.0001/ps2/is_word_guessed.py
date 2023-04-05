#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:45:30 2023

@author: hanpeitao
"""
import string
def is_word_guessed(secret_word, letters_guessed):
    list_of_word = list(set(secret_word))
    # print(list_of_word)
    for letter in letters_guessed:
        if letter in list_of_word:
            list_of_word.remove(letter)
    if not list_of_word:
        return True
    else:
        return False
    
def get_guessed_word(secret_word, letters_guessed):
    list_of_word = list(secret_word)
    clue = []
    for i in range(len(list_of_word)):
        clue.append('_ ')
    #print(''.join(clue))
    for letter in letters_guessed:
        if letter in list_of_word:
            # index = list_of_word.index(letter)
            indices = [i for i, x in enumerate(list_of_word) if x == letter]
            for i in indices:
                clue[i] = letter
    return(''.join(clue))

def get_available_letters(letters_guessed):
    list_of_lowercase = list(string.ascii_lowercase)
    for letter in letters_guessed:
        list_of_lowercase.remove(letter)
    return ''.join(list_of_lowercase)
    
def hangman(secret_word):
    guess = 6
    warning = 3
    letters_guessed = []
    print('Welcome to the game Hangman! ')
    print('I am thinking of a word that is {} letters long.  '.format(len(secret_word)))
    print('------------- ')
    while guess:
        print('You have {} warnings left. '.format(warning))
        print('You have {} guesses left. '.format(guess))
        print('Available letters: ' ,get_available_letters(letters_guessed))
        print('Please guess a letter: ')
        letter = input()
        if not letter.isalpha():
            if warning > 0:
                warning -= 1
            else:
                guess -= 1
            print('Oops! That is not a valid letter. You have {} warnings left:'.format(warning) ,get_guessed_word(secret_word, letters_guessed))
            print('------------- ')
            continue
        if letter in letters_guessed:
            if warning > 0:
                warning -= 1
            else:
                guess -= 1
            print('OOops! You\'ve already guessed that letter. You have {} warnings left:'.format(warning) ,get_guessed_word(secret_word, letters_guessed))
            print('------------- ')
            continue
        letters_guessed.append(letter)
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won! ')
            print('Your total score for this game is: ' , guess * len(set(secret_word)))
            break
        else:
            if letter in list(secret_word):
                print('Good guess: ' ,get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That letter is not in my word: ' ,get_guessed_word(secret_word, letters_guessed))
        print('------------- ')
        guess -= 1
        
    print('Sorry, you ran out of guesses. The word was {}. '.format(secret_word))
    

secret_word = 'apple'
hangman(secret_word)
