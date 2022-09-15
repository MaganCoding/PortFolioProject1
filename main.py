# Get all the letters in the alphabet
abcs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Get the morse code alphabet
morse_code = ['.- ', '-... ', '-.-. ', '-.. ', '. ', '..-. ', '--. ', '.... ', '.. ', '.--- ', '-.- ', '.-.. ', '-- ', '-. ', '--- ', '.--. ', '--.- ', '.-. ', '... ', '- ', '..- ', '...- ', '.-- ', '-..- ', '-.-- ', '--.. ']

#Get the numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Get the morse code numbers
morse_numbers = ['----- ', '.---- ', '..--- ', '...-- ', '....- ', '..... ', '-.... ', '--... ', '---.. ', '----. ']

#Get all the characters (includes space)
characters = [' ', '.', ',', '?', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@']

#Get all the characters in morse
morse_chars = ['/ ', '.-.-.- ', '--..-- ', '..--.. ', '.----. ', '-.-.-- ', '-..-. ', '-.--. ', '-.--.- ', '.-... ', '---... ', '-.-.-. ', '-...- ', '.-.-. ', '-....- ', '..--.- ', '.-..-. ', '...-..- ', '.--.-. ']

#Get the users input and keep it lowercase. Then convert it to a list as well.
string_to_convert = input('Type something you want in morse code: ').lower()
string_list = list(string_to_convert)

#This line of code below was to test to see whether the letters numbers and characters were all the same length.
# print(f"{len(abcs)} letters and {len(morse_code)} morse letters. {len(numbers)} numbers and {len(morse_numbers)} morse numbers. {len(characters)} characters and {len(morse_chars)} morse characters")

#Create an empty list
answer = []

#Check to see which list the input needs to go to and append to the created list above.
for string in string_list:
    if string in abcs:
        in_abcs = abcs.index(string)
        answer.append(morse_code[in_abcs])
    elif string in numbers:
        in_numbers = numbers.index(string)
        answer.append(morse_numbers[in_numbers])
    elif string in characters:
        in_chars = characters.index(string)
        answer.append(morse_chars[in_chars])

answer_in_string = ' '.join([str(elem) for elem in answer])
print(answer_in_string)
