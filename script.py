import os
from pathlib import Path


# print the file names in the directory
def get_files(dir_path):
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.txt')]

dir_path = os.getenv ("DATAPATH", str(Path(__file__).parent))

# cwd = os.getcwd()
# dir_path = f"{cwd}"

files = get_files(dir_path)
num_files = len(files)
output_1 = f'list of files in {dir_path}: {files}, number of files: {num_files}\n'
# print(f'list of files in {dir_path}: {files}, number of files: {num_files}\n')
# write to file



# coumts the number of words in each file and sums the count 
def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

file1 = f"{dir_path}/limerick.txt" 
file2 = f"{dir_path}/IF.txt" 

num_words_file1 = count_words(file1)
num_words_file2 = count_words(file2)
total_num_words_in_both_files = num_words_file1 + num_words_file2

output_2 = f'Number of words in {file1}: {num_words_file1}'
output_3 = f'Number of words in {file2}: {num_words_file2}'
output_4 = f'Total number of words in both files: {total_num_words_in_both_files}\n'



# Get three(3) words having highest frequencies in 'IF.txt'
filename1 = "IF.txt" # replace with your filename
word_freq = {}

with open(filename1, 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

# sort the words by frequency
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)


# print the top 3 words with their counts
output_5 = 'Top three(3) words in IF.txt with the highest frequencies'
output_all = {}
for x in range(3): 
    word, count = sorted_words[x]
    output_all[x]= f"{word}: {count}"

output_6 = str(output_all.values())


# use cmd and / to comment
# Find the ip address of this machine
import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

output_7 = "\nYour machine IP address is: " + host_ip+'\n'


# write output to file
output_list = [output_1, output_2, output_3, output_4, output_5, output_6, output_7]  
file_path = f"{dir_path}/output.txt"  

with open(file_path, "a") as file:
    for output_items in output_list:
        file.write(output_items+'\n')
