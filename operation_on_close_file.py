file_name = 'example.txt'

with open(file_name, 'w', encoding='utf-8') as my_file:
    my_file.write('first line' + '\n')

print(my_file.closed)  # 👉️ True

# 👇️ forgot to indent the code

# ⛔️ ValueError: I/O operation on closed file.
my_file.write('second line' + '\n')
my_file.write('third line' + '\n')
