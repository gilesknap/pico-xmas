from morse.morse_code import morse_code, translate

# do 1000 happy xmas's
message, repeat = "happy christmas everyone   ", 1000

my_morse = translate(message)
print(f"Playing '{message}' {repeat} times.\n Morse code is: {my_morse}")

morse_code(my_morse, 1000)
