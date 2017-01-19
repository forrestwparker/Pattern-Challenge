# Pattern-Challenge

The first two functions of Pattern.py constitute a solution to the following challenge:

Write a function that accepts a string such as "onetwothreefourcowcowcowcow" and another string such as "abcdeeee" that returns true if there is a substitution that can be applied to the characters in the second string to produce the first string and so that distinct characters from the second string are replaced by distinct strings in the substitution.

For the given example, the substitution 'a' -> "one", 'b' -> "two", 'c' -> "three", 'd' -> "four", 'e' -> "cow" shows that the function should return True in this case.


The rest of the code is my implementation of part of an approach taken by an associate who attempted the challenge. Although it works quickly for short strings, it is not efficient as it requires an exponential amount of memory (and computation) proportional to the length of the string it is given. It has been artificially handicapped to prevent locking up a computer accidentally.