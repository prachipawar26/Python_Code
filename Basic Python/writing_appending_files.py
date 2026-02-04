# open file names 'file.txt'; modes ---> r = read, w = write, a = append, r+ = read & write
# demo_file = open("./Basic Python/demo.txt", "a") 
demo_file = open("./Basic Python/demo.txt", "w") 
demo_file.write("\nThis is fourth line of the file") # changes file.txt
# on each run the new line will be appended when in "a" mode
# on each run will overwrite the existing file when in "w" mode
demo_file.close()

# creating new file
demo_file2 = open("./Basic Python/demo.html", "w")
demo_file2.write("<p> This is HTML </p>")
