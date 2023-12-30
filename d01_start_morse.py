from morse.morse_code import morse_code, translate

# do 1000 happy xmas's
message, repeat = "happy christmas everyone   ", 1000

my_morse = translate(message)
morse_print = " ".join(my_morse)
print(f"Playing '{message}' {repeat} times.\n{morse_print}")

morse_code(my_morse, repeat)
