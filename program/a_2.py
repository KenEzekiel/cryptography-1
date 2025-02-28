
# Ekstraksi file
with open('./data/ciphertext-a.txt', 'r') as file:
  data = file.read()
  data = data.strip().replace('\n', '').replace(' ', '')
  # print(data)
  
# Menggunakan hasil dari analisis freq
# mapper = {
#     "E": "e",
#     "V": "t",
#     "Y": "a",
#     "U": "o",
#     "P": "i",
#     "I": "n",
#     "M": "s",
#     "B": "h",
#     "A": "r",
#     "N": "d",
#     "K": "l",
#     "X": "u",
#     "G": "c",
#     "O": "m",
#     "F": "f",
#     "R": "w",
#     "H": "g",
#     "T": "y",
#     "S": "p",
#     "L": "b",
#     "Z": "v",
#     "W": "k",
#     "C": "x",
#     "J": "j",
#     "Q": "q"
# }

mapper = {
     "E": "e",
     "V": "t",
     "A": "h",
     "P": "a",
     "Y": "s",
     "B": "r",
     "W": "v",
     "F": "m",
     "S": "g",
     "M": "n",
     "N": "c",
     "U": "i",
     "G": "l",
     "O": "y",
     "K": "p",
     "I": "o",
     "R": "u",
     "T": "f",
     "H": "d",
     "X": "b",
     "Z": "w",
     "J": "q",
     "L": "k",
     "C": "x",
     "Q": "j"
}

# Dekripsi teks
decrypted = ''
for char in data:
  if char in mapper.keys():
    decrypted += mapper[char]
  else:
    decrypted += char



# Tulis hasil ke file txt
# print(decrypted)
with open('./data/decrypted-a.txt', 'w') as file:
  file.write(decrypted)