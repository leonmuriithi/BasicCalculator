# Read from one file and write modified content to another
with open("input.txt", "r") as infile:
    content = infile.read()

#make all text uppercase
modified_content = content.upper()

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)