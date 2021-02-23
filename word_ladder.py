#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    from collections import deque
    import copy

    with open(dictionary_file) as f:
        words = f.readlines()
        words = list(set([word.strip() for word in words]))

    if start_word == end_word:
        return [start_word]

    stack = []
    stack.append(start_word)

    queue = deque()
    queue.append(stack)

    while len(queue) != 0:
        latest = queue.popleft()
        for word in words:
            if _adjacent(word, latest[-1]):
                s2 = copy.copy(latest)
                s2.append(word)
                if word == end_word:
                    return s2
                queue.append(s2)
                words.remove(word)
    return


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    checker = [1 for i in range(len(ladder) - 1)
               if _adjacent(ladder[i], ladder[i + 1])]
    count = checker.count(1)

    return count == len(ladder) - 1


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    # Base cases
    if word1 == word2:
        return False
    elif len(word1) != len(word2):
        return False
    else:
        w1 = list(word1)
        w2 = list(word2)

        w3 = list(map(list, zip(w1, w2)))
        w4 = [w[0] for w in w3 if w[0] == w[1]]

        return len(w4) == len(w3) - 1
