import os
from collections import Counter
import socket

# Function to list files in a directory
def files_of_directory(directory):
    files = os.listdir(directory)
    text_files = [file for file in files if file.endswith('.txt')]
    return text_files

# Function to count words in a text file
def file_word_count(file_path):
    with open(file_path, 'r') as file:
        script = file.read()
        words = script.split()
        return len(words)

# Function to find top n words with their counts in a given text file
def top_n_words_in_file(file_path, n=3):
    with open(file_path, 'r') as file:
        script = file.read()
        words = script.split()
        count_of_words = Counter(words)
        top_words_count = count_of_words.most_common(n)
        return top_words_count

# Function to get host IP address
def get_host_ip():
    return socket.gethostbyname(socket.gethostname())

# Main function
def main():
    # List files
    files = files_of_directory('/home/data')
    with open('/home/output/result.txt', 'w') as output_file:
        # Write list of files
        output_file.write("List of files in /home/data:\n")
        for file in files:
            output_file.write(file + '\n')
        
        # Count words in each text file and calculate grand total
        grand_total = 0
        output_file.write("\nWord counts:\n")
        for file in files:
            file_path = os.path.join('/home/data', file)
            if file in ['IF.txt', 'Limerick-1.txt']:
                word_count = file_word_count(file_path)
                output_file.write(f"Number of words present in {file}: {word_count} words\n")
                grand_total += word_count
        output_file.write(f"Total number of words in both the files, grand total: {grand_total} \n")
            
        # Find top 3 words in IF.txt
        if_file_path = '/home/data/IF.txt'
        top_words_result = top_n_words_in_file(if_file_path, n=3)
        output_file.write("\nTop 3 words with maximum counts in IF.txt:\n")
        for word, count in top_words_result:
            output_file.write(f"{word}: {count} times\n")
        
        # Find host IP address
        host_ip = get_host_ip()
        output_file.write("\nHost IP address:\n")
        output_file.write(host_ip)

        # Open the result.txt file and print its contents
    with open('/home/output/result.txt', 'r') as result_file:
        result_content = result_file.read()
        print("Contents of result.txt:")
        print(result_content)

if __name__ == "__main__":
    main()
