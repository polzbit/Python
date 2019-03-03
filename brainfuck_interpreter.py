
# >	INCREMENT THE DATA POINTER (TO POINT TO THE NEXT CELL)
# <	DECREMENT THE DATA POINTER (TO POINT TO THE PREVIOUS CELL)
# +	INCREMENT (INCREASE BY ONE) THE VALUE OF THE BYTE AT THE DATA POINTER
# -	DECREMENT (DECREASE BY ONE) THE VALUE OF THE BYTE AT THE DATA POINTER
# .	OUTPUT THE BYTE AT THE DATA POINTER
# ,	ACCEPT ONE BYTE OF INPUT, STORING ITS VALUE IN THE BYTE AT THE DATA POINTER
# [	IF THE BYTE AT THE DATA POINTER IS ZERO, THEN JUMP FORWARD TO THE COMMAND AFTER THE MATCHING ] COMMAND
# ]	IF THE BYTE AT THE DATA POINTER IS NONZERO, THEN JUMP BACK TO THE COMMAND AFTER THE MATCHING [ COMMAND

s1=">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++."
# Hello World

def brainFuck(str):
    i=1
    a = [0] * 25
    count =0
    l=0
    while l < len(str):
        if str[l] == ">":
            i+=1
        elif str[l] == "<":
            i-=1
        elif str[l] == "+":
            a[i] = a[i] + 1 & 0xFF
        elif str[l] == "-":
            a[i] = a[i] - 1 & 0xFF
        elif str[l] == ".":
            print "OUTPUT: %d" % (a[i])
        elif str[l] == ",":
            n = raw_input("Enter input number: ")
            a[i] = int(n)
        elif str[l] == "[":
            if a[i] == 0:
                while str[l] != "]":
                    l+=1            
        elif str[l] == "]":
            if a[i] != 0:
                while str[l] != "[":
                    l -= 1     
        l+=1
        count+=1
    print a

def main():
    brainFuck(s1)

if __name__ == "__main__": main()