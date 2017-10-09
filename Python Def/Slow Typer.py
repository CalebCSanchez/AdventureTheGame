import sys,time #must import these at begining of program.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1) #How fast it types. Higher the number slower it goes.
print_slow("Type whatever you want here.")
