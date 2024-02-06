import os
def nucleotideCounter():
    nucleotide_dic = {
            "A": 0,
            "G": 0,
            "C": 0,
            "T": 0
        }
    with open("input", "r") as file:
        for line in file:
            blank = line.strip()
            for letter in blank:
                if letter == 'A':
                    nucleotide_dic['A'] += 1
                elif letter == 'G':
                    nucleotide_dic['G'] += 1
                elif letter == 'C':
                    nucleotide_dic['C'] += 1
                elif letter == 'T':
                    nucleotide_dic['T'] += 1
    # Open the file in write mode
    with open("output", "w") as file:
        # Write 4 integers separated by spaces to the file
        file.write(str(nucleotide_dic['A']) + " " + str(nucleotide_dic['C']) + " " + str(nucleotide_dic['G']) + " " + str(nucleotide_dic['T']))
if __name__ == "__main__":
    # Call the function if the script is executed directly
    nucleotideCounter()
        
    
            
