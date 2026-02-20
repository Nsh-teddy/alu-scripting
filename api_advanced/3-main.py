#!/usr/bin/python3
"""
3-main - Test count_words function
"""
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 3-main.py <subreddit> '<word1> <word2> ...'")
    else:
        count_words = __import__('3-count').count_words
        subreddit = sys.argv[1]
        words = sys.argv[2].split()
        count_words(subreddit, words)
