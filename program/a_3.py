import re
from collections import Counter

def extract_and_count(filename, pattern):
    # Read the content of the file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Find all matches of the pattern
    matches = re.findall(pattern, content)
    
    # Count the frequencies of the matched strings
    frequency = Counter(matches)
    
    return frequency

# Example usage
filename = './data/decrypted-a.txt' 
pattern = r'the[A-Z]e' 

frequency = extract_and_count(filename, pattern)
for match, count in frequency.items():
    print(f'{match}: {count}')