

# Function to save file from input
def save_file():
    try:
        outfile = open('running_times.txt', 'w')
        numOfVideo = int(input('Enter the number of videos: '))
        for i in range(numOfVideo):
            time= int(input('Enter the running time: '))
            outfile.write(str(time)+'\n')
        outfile.close()
    except TypeError as t:
        print(t)
    except ValueError as v:
        print(v)

# Function to read data from the file
def read_contents():
    try:
        total = 0
        infile = open('running_times.txt', 'r')
        line = infile.readline()
        while line != '':
            line = line.rstrip('\n')
            number = int(line)
            total += number
            line = infile.readline()
        infile.close()
    except FileNotFoundError as f:
        print(f)
    # Print the result
    minute = total//60
    second = total % 60
    print('Total running time is:',minute,'min', second, 'sec')

# Main function
def main():
    save_file()
    read_contents()
main()
