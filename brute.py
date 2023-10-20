

text = "900802jfeng@veryrealmail.com%R3ply!"

file_path = "combinations.txt"  

# Open the file in read mode
with open(file_path, 'r') as file:
    content = file.readlines()

for line in content:
    new_text = text.replace('%', line.strip())
    print(new_text)


