# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, 'r')  # opens file in for reading
    content = file.read()  # extracts content of the file
    file.close()  # closes file
    return content


def count_words():
    # [assignment] Add your code here
    text = read_file_content("./story.txt")
    words = text.split()  # Changes the text into a list

    new_words = "God is Good is"
    new_words = new_words.split()

    dic = {}  # Define an empty dictionary
    for word in words:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1

    print(dic)


count_words()
