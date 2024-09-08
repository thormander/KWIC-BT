from collections import deque

class Pipe:
    def __init__(self):
        self.buffer = deque() # will give us a O(1) or constant time appends and pops
    
    def put(self, item):

        self.buffer.append(item)
    
    def get(self):

        while len(self.buffer) == 0:
            pass  # Here we just wait until there is some data available

        return self.buffer.popleft()

class Filter:
    def __init__(self, inputP, outputP):

        self.inputP = inputP
        self.outputP = outputP

class Input(Filter):
    def __init__(self, outputP, lines):
        
        self.outputP = outputP
        self.lines = lines
    
    def run(self):

        i = 0

        while i < len(self.lines):
            #add lines to stream
            line = self.lines[i]
            self.outputP.put(line)
            i += 1

        self.outputP.put(None)  # to signal end of our input pipe

class CircularShifter(Filter):
    def run(self):

        while True:
            #stream from prev pipe.
            line = self.inputP.get()
            if line is None:
                self.outputP.put(None)
                break
            #get the words in the line
            words = line.split()

            for i in range(len(words)):

                shifted_words = []
                # we need to shift the words (this is the same logic as object)

                #move current->end to the front
                for j in range(i, len(words)):
                    shifted_words.append(words[j])
                
                #then add the start->current to list
                for k in range(i):
                    shifted_words.append(words[k])

                # jion them together.

                shifted_line = ''

                for word in shifted_words:
                    if shifted_line == '':
                        shifted_line = word
                    else:
                        shifted_line = shifted_line + ' ' + word
                        
                self.outputP.put(shifted_line)

class Alphabetizer(Filter):
    def run(self):

        shifts = []
        #we need while loops in the pipe as its more streaming the data. So from the stream we want to sort the lines.
        while True:
            #get hte line. 
            shift = self.inputP.get()

            if shift is None:
                shifts = sorted(shifts)  #sort them. this may happen a few times
                
                i = 0
                while i < len(shifts):

                    self.outputP.put(shifts[i])    
                    i += 1

                self.outputP.put(None) #end our stream
                break

            shifts.append(shift)


class Output(Filter):
    """
    This class is responsible for printing the outputs
    """
    def __init__(self, inputP):
        #definet he input pipe
        self.inputP = inputP
    
    def run(self):
        
        #loop until the pipe is done
        while True:

            line = self.inputP.get()

            if line is None:
                break

            print(line)

if __name__ == "__main__":

    # with this input, we should expect 12 lines of output in our console
    lines = [
        "this is a test",
        "another test line",
        "one more line for testing"
    ]

    # Create pipes to connect the filters
    inputP = Pipe()  # input pipe
    shifter_pipe = Pipe()  #input pipe
    sorter_pipe = Pipe()  # alphebetizer pipe. 

    # Make sure our filters have correct pipes.

    input_filter = Input(outputP=inputP, lines=lines)

    shifter_filter = CircularShifter(inputP=inputP, outputP=shifter_pipe)
    alphabetizer_filter = Alphabetizer(inputP=shifter_pipe, outputP=sorter_pipe)
    
    output_filter = Output(inputP=sorter_pipe)

    # Now we can finally run our filters on 'lines' variable
    input_filter.run()

    shifter_filter.run()
    alphabetizer_filter.run()

    output_filter.run()
