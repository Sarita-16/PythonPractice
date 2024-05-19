def fullJustify(words, maxWidth):
    result = []
    line = []
    num_of_letters = 0

    for word in words:
        if num_of_letters + len(word) + len(line) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                line[i % (len(line) - 1 or 1)] += ' '
            result.append(''.join(line))
            line = []
            num_of_letters = 0
        line.append(word)
        num_of_letters += len(word)

    result.append(' '.join(line).ljust(maxWidth))
    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = fullJustify(words, maxWidth)
for line in output:
    print(f'"{line}"')
