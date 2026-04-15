'''Returns frequency of characters in a sentence excluding spaces.'''
def key_value(sentence):
    freq = {} 

    for char in sentence:
        if char != " ":  
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    return freq

text = input("Enter a sentence: ")

result = key_value(text)

print("\nCharacter frequency (excluding spaces):")
print(result)