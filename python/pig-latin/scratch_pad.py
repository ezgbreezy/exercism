text = "xray yttria"
text = text.lower().split()

# Define sounds
consonants = [
    'b', 'c', 'd', 'f', 'g', 
    'h', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 'r', 's', 
    't', 'v', 'w', 'x', 'y'
    'z' 
]
vowels = ['a', 'e', 'i', 'o', 'u']  

# Define pig-latin suffix
suffix = "ay"

# Loop through words in text
for word in text:
    
    # Reset cluster and 'y' vowel status
    cluster = ""
    if vowels.count('y') > 0:
            vowels.remove('y')
    if consonants.count('y') < 1:
            consonants.append('y')

    # Loop through letters in word
    for letter in word:
        if len(cluster) == 1:
            vowels.append('y')
            consonants.remove('y')
        if letter in consonants:
            # 'xr' edge case handling
            if (letter == 'r' and cluster.endswith('x')):
                cluster = ""
                word = word + suffix
                break
            # 'yt' edge case handling
            elif letter == 't' and cluster.endswith('y'):
                cluster = ""
                word = word + suffix
                break
            cluster += letter
        elif letter in vowels:
            # 'qu' edge case handling
            if letter == 'u' and cluster.endswith('q'):
                cluster += letter
                word = word.removeprefix(cluster) + cluster + suffix
                break
            # 'yt' edge case handling
            elif letter == 't' and cluster.endswith('y'):
                cluster = ""
                word = word + suffix
                break
            else:
                word = word.removeprefix(cluster) + cluster + suffix
                break
    print(f"{word} ", end="")
print()

