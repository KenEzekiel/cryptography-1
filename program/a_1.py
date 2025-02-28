
# Ekstraksi file
with open('./data/ciphertext-a.txt', 'r') as file:
  data = file.read()
  data = data.strip().replace('\n', '').replace(' ', '')
  print(data)
  
# Analisis frekuensi huruf
freq_letter = {}
for char in data:
  if char in freq_letter:
    freq_letter[char] += 1
  else:
    freq_letter[char] = 1

# Sort frekuensi
freq_letter = dict(sorted(freq_letter.items(), key=lambda item: item[1], reverse=True))

# Print hasil
for key, value in freq_letter.items():
  print(f'{key} : {value}')
  
# Analisis frekuensi bigram
freq_bigram = {}
for i in range(len(data)-1):
  bigram = data[i:i+2]
  if bigram in freq_bigram:
    freq_bigram[bigram] += 1
  else:
    freq_bigram[bigram] = 1

# Sort frekuensi
freq_bigram = dict(sorted(freq_bigram.items(), key=lambda item: item[1], reverse=True))

# Print hasil
for key, value in freq_bigram.items():
  print(f'{key} : {value}')
  
# Analisis frekuensi trigram
freq_trigram = {}

for i in range(len(data)-2):
  trigram = data[i:i+3]
  if trigram in freq_trigram:
    freq_trigram[trigram] += 1
  else:
    freq_trigram[trigram] = 1

# Sort frekuensi
freq_trigram = dict(sorted(freq_trigram.items(), key=lambda item: item[1], reverse=True))

# Print hasil
for key, value in freq_trigram.items():
  print(f'{key} : {value}')

# Tulis hasil ke file txt
with open('./data/freq_a.txt', 'w') as file:
  i = 1
  for key, value in freq_letter.items():
    file.write(f'{i}. {key} : {value}\n')
    i += 1
  i = 1
  for key, value in freq_bigram.items():
    file.write(f'{i}. {key} : {value}\n')
    i += 1
  i = 1
  for key, value in freq_trigram.items():
    file.write(f'{i}. {key} : {value}\n')
    i += 1