from collections import Counter

if __name__ == '__main__':
    s = input()

    results = sorted(
        Counter(s).items(),
        key=lambda item: (-item[1], item[0])
    )

    for character, frequency in results[:3]:
        print(character, frequency)

  ## non lambda version 

def get_frequency(item):
    return item[1]


if __name__ == '__main__':
    s = input()

    counts = {}

    # Count every character
    for character in s:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1

    # Convert the dictionary into a list
    results = list(counts.items())

    # First put characters in alphabetical order
    results.sort()

    # Then sort by frequency, highest first
    results.sort(key=get_frequency, reverse=True)

    # Print the first three
    for character, frequency in results[:3]:
        print(character, frequency)
