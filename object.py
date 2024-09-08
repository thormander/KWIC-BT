class KWIC:
    # stores lines of text and stuff
    def __init__(self):
        self.lines = [] # this is where we store the lines

    def add_line(self, line):

        self.lines.append(line) # add a line to the list

    def get_lines(self):

        return self.lines # return the list of lines


class CircularShifter:
    # this class generates all shifts of stored lines., We shift each words in the line such that each word will come first. 
    def __init__(self, list_of_input_words):

        self.list_of_input_words = list_of_input_words

        self.shifts = [] # this is where we store the shifts

    def generate_shifts(self):

        lines = self.list_of_input_words.get_lines()

        #we for loop over each line and split the words. 
        for line in lines:

            words = line.split() # split the line into the words

            #loop through each word inthe line
            for i in range(len(words)):

                shifted_words = [] # this is where we store the shifted words

                #For each iteration it creates a new shfited version of th eline. we shift current to front and anythign before current->end.

                for j in range(i, len(words)):
                    
                    shifted_words.append(words[j]) # add the word to the list
                
                #now we add the words that are before the current word in the list.
                for k in range(0, i):
                    shifted_words.append(words[k]) # add the word to the list


                shifted_line = '' # this is where we store the shifted line

                #now we can create the new shifted line by joining the words back together.
                for word in shifted_words:

                    if shifted_line == '':
                        shifted_line = word
                    else:
                        
                        shifted_line= shifted_line+ ' '+ word # add the word to the shifted line

                self.shifts.append(shifted_line) # add the shifted line to the list

    def get_shifts(self):
        return self.shifts # return the list of shifts
class Alphabetizer:
    # this class sorts lines alphabetically descending
    def __init__(self, input_shifts):

        self.input_shifts = input_shifts

        self.sorted_shifts = [] # return this later with sorted answer

    def sort(self):
        self.sorted_shifts = sorted(self.input_shifts) # sort the input shifts

    def get_sorted_shifts(self):

        return self.sorted_shifts # return the list of sorted shifts


class Output:
    # this class displays sorted lines
    def __init__(self, lines):

        self.lines = lines # this is where we store the lines

    def print_output(self):
        for i in range(len(self.lines)):

            print(self.lines[i]) # print the line


def main():
    # createa KWIC Objhect to which we can add lines for shifting and ordering.
    list_of_input_words = KWIC()


    #add oru test cases.
    list_of_input_words.add_line("this is a test")
    list_of_input_words.add_line("another test line")
    list_of_input_words.add_line("one more line for testing")

    # create a shifter and generate shifts. This will tierate through and reorder each line so that each word comes first.
    shifter = CircularShifter(list_of_input_words)

    shifter.generate_shifts()

    # create an alphabetizer to first get all ore shifts form the input; we want to use the first letter of each "shift".
    alphabetizer = Alphabetizer(shifter.get_shifts())

    alphabetizer.sort() # and then we call on the sort once we get those shifts

    # create an output object to display the shjifts.
    output = Output(alphabetizer.get_sorted_shifts())
    output.print_output()


if __name__ == "__main__":
    main()
