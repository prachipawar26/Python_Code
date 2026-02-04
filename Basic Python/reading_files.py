# open file names 'file.txt'; modes ---> r = read, w = write, a = append, r+ = read & write, rb = read binary file, wb = write binary file
demo_file = open("./Basic Python/demo.txt", "r") 
print(demo_file.readable()) # returns True
print(demo_file.read()) # reads whole file
print(demo_file.readline()) # reads next line of the file
print(demo_file.readline(), end="") # removes newline
print(demo_file.readlines()) # all lines are put inside an array (if not already read)
print(demo_file.readlines()[1]) # read only line at 1st index
demo_file.close()

# for loop can be used to read multiple lines
# Best practice to close a file whenever opened
