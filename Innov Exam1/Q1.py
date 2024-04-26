programming_lang = input("What is your programming Language? ")
input_language = programming_lang.lower()
if input_language == 'python':
    print("Python")
elif input_language == 'java':
    print("Java")
elif input_language == 'c++':
    print("C++")
elif input_language == 'javascript':
    print("JavaScript")
elif input_language == 'php':
    print("PHP")
else:
    print("Language not found.")