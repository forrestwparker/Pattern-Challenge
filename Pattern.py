# Created by:
# Forrest W. Parker
# 01/06/2017
#
# Version 1.0
# 01/06/2017

#####

import math


# Returns True if the string 'string' matches the pattern string 'patstring'
# and returns False otherwise.
#
# Note that distinct characters of 'patstring' must correspond to
# distinct substrings of 'string'.
# (e.g. "a" and "b" in 'patstring' cannot both correspond to the
# substring "one" in 'string')
#
# Examples:
# >>> checkPattern("onetwothreefourcowcowcowcow","abcdeeee")
# True
# >>> checkPattern("onetwothreefourcowcowcowcow","abcdeeff")
# False
# >>> checkPattern("onetwothreefourcowcowcowcow","abcdeef")
# True
#
# Note that neither 'string' nor 'patstring' are restricted
# to alphabetical characters.

def checkPattern (string, patstring):
    return checkPatternRecursive(string, patstring, {})


# Used by checkPattern.
# See the notes throughout for details about how it works.

def checkPatternRecursive (string, patstring, patdict):
    
    # First check if either 'string' or 'patstring' is empty.
    # If either is empty, go to the elif statement far below.
    #
    # Otherwise both are nonempty, do the following.
    if len(string) != 0 and len(patstring) != 0:
        
        # Take the first character in 'patarray'.
        patletter = patstring[0]
        
        # If this character is already assigned to a string in 'patdict',
        # do the following.
        if patletter in patdict.keys():
            
            # Get the string assigned to 'patletter'.
            sub = patdict[patletter]
            
            # If 'sub' is longer than 'string' or
            # if string does not start with sub,
            # the current set of character substitutions
            # has failed, so return False.
            if len(string) < len(sub) or sub != string[:len(sub)]:
                return False
            
            # Else the character substitution made earlier
            # is still acceptable, so call checkPatternRecursive
            # again with 'sub' removed from the the beginning of
            # 'string' and 'patletter' removed from the beginning
            # of 'patstring' and return the result.
            else:
                return checkPatternRecursive(string[len(sub):], patstring[1:], patdict)
            
        # Else 'patletter' is not assigned to a string in 'patdict',
        # so initialize 'fitsPattern', 'subLength', and 'maxLength'.
        else:
            fitsPattern = False
            subLength = 0
            maxLength = math.floor((len(string)-len(patstring)+patstring.count(patletter))
                                   /patstring.count(patletter))

            # Incrementally increase 'subLength' by one and let 'sub'
            # be the substring formed by the first 'subLength' characters
            # of 'string' with a maximum length of 'maxLength'.
            #
            # Note that the calculation of 'maxLength' determines the longest
            # substring of 'string' that can be substituted for 'patletter'
            # before the substitution cannot be valid.
            #
            # If during any iteration 'fitsPattern' is set to True, cease
            # future iterations.
            while subLength < maxLength and not fitsPattern:
                subLength += 1
                sub = string[:subLength]

                # If 'sub' is already assigned to a different character in
                # 'patdict', skip it.
                #
                # Otherwise, create a new entry in 'patdict' to record the
                # new substitution, assign 'fitsPattern' to be the result
                # of calling checkPatternRecursive again with 'sub'
                # removed from the the beginning of 'string' and
                # 'patletter' removed from the beginning of 'patstring',
                # and finally remove the 'patletter'-'sub' pairing from
                # 'patdict'.
                #
                # Note that the last step is necessary since dictionaries
                # are passed into functions by reference, not by value. Not
                # removing the pairing may cause errors to future calls
                # of checkPatternRecursive as 'patdict' would contain entries
                # made in earlier iterations, leading to incorrect results.
                if not sub in patdict.values():
                    patdict[patletter] = sub
                    fitsPattern = checkPatternRecursive(string[subLength:], patstring[1:], patdict)
                    patdict.pop(patletter)

            # Once finished considering substitutions for 'patletter'
            # (whether successful or not), return 'fitsPattern'.
            return fitsPattern
        
    # Else either 'string' or 'patstring' is an empty string.
    # If both are empty, then a successful set of substitutions
    # has been found, so return True.
    elif len(string) == 0 and len(patstring) == 0:
        return True
    
    # Else only one of 'string' and 'patstring' is empty.
    # This indicates that the current set of substitutions
    # is not valid, so return False.
    else:
        return False


#####

# Returns with an array of stringpattern classes which contain all
# patternArrays and corresponding patternDictionaries for the string
# 'string'.
#
# WARNING: This function would use an exponential amount of memory
# proportional to the length of 'string'. It has been artificially
# capped to run properly only when 'string' has no more than eight
# characters.

def findAllPatterns(string):
    if len(string) > 8:
        return []
    else:
        return findAllPatternsRecursive(string, {}, {})


# Used by findAllPatterns.
# Functionality is left to the reader to determine.

def findAllPatternsRecursive(string, patdict, valdict):
    patarray = []
    if len(string) == 0:
        patarray.append(stringpattern(patdict))
    else:
        for i in range(0,len(string)):
            n = len(string)-i
            sub = string[:n]
            if sub in valdict.keys():
                patnum = valdict[sub]+1
                isNewNum = False
            else:
                patnum = len(patdict.keys())+1
                patdict[str(patnum)] = sub
                valdict[sub] = patnum
                isNewNum = True
            getpatarray = findAllPatternsRecursive(string[n:], patdict.copy(), valdict.copy())
            for j in getpatarray:
                j.patternArray.insert(0,patnum)
            patarray.extend(getpatarray)
            if isNewNum:
                patdict.pop(str(patnum))
                valdict.pop(sub)
    return patarray


# Class used by findAllPatterns

class stringpattern:
    def __init__(self, patdict):
        self.patternArray = []
        self.patternDictionary = patdict.copy()

    def makeString(self):
        string = ""
        for i in self.patternArray:
            string += self.patternDictionary[str(i)]
        return string
