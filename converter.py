def c_to_f(celsius):
    return (celsius * 9 / 5) + 32

def fto_c(fahrenheit):
    return (fahrenheit -32) * 5/9

def main():
    user = int(input("Do you want to convert from f or c: "))
    if user == 1:
        celsius = int(input("How many do you want to convert: "))
        fahrenheit = c_to_f(celsius)
        print(f"fahrenheit: {fahrenheit} and your celsius : {celsius}!")
    elif user == 2:
       fahrenheit = int(input("How many do you want to convert: "))
       celsius = c_to_f(fahrenheit)
       print(f"fahrenheit: {celsius} and your celsius : {fahrenheit}!")

main()