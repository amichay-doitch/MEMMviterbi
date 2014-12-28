import re, os, sys

def form(line):
    pattern = "\(([^\(\)]+)\)"
    return re.findall(pattern,line)

def format(filename):
    FILENAME, fileExtension = os.path.splitext(filename)
    output = open(FILENAME + "_pos" + fileExtension,'w')
    f = open(filename,'r')
    f = f.readlines()
    for line in f:
        o = form(line)
        output.write("\n".join(o))
        output.write("\n\n")
        
def main():
    filename = sys.argv[1]
    format(filename)
    
if __name__ == "__main__":
    main()
