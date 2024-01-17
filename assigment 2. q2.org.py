# Generate a number using the current time
import time
from PIL import Image

current_time = int(time.time())
generated_number = (current_time % 100) + 50

# Add 10 to the generated number if it's even
if generated_number % 2 == 0:
    generated_number += 10

print("Generated Number:", generated_number)

# Load the image
image_path = 'Chapter1.png'
image = Image.open(image_path)

# Modify the image pixels by adding the generated number
for i in range(image.width):
    for j in range(image.height):
        r, g, b = image.getpixel((i, j))
        new_r = r + generated_number
        new_g = g + generated_number
        new_b = b + generated_number
        image.putpixel((i, j), (new_r, new_g, new_b))

# Save the modified image
output_image_path = 'chapter1out.png'
image.save(output_image_path)

# Calculate the sum of red pixel values in the new image
red_pixel_sum = sum([image.getpixel((i, j))[0] for i in range(image.width) for j in range(image.height)])

print("Sum of red pixel values:", red_pixel_sum)
part 2 
# Given string
string = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# Separate the string into number and letter substrings
number_string = ''.join(filter(str.isdigit, string))
letter_string = ''.join(filter(str.isalpha, string))

# Convert even numbers in the number string to ASCII Code Decimal Values
even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
ascii_values_even_numbers = [ord(str(num)) for num in even_numbers]

# Convert upper-case letters in the letter string to ASCII Code Decimal Values
uppercase_letters = [char for char in letter_string if char.isupper()]
ascii_values_uppercase_letters = [ord(char) for char in uppercase_letters]

# Print the results
print("Number String:", number_string)
print("Letter String:", letter_string)
print("Even Numbers:", even_numbers)
print("ASCII Values of Even Numbers:", ascii_values_even_numbers)
print("Uppercase Letters:", uppercase_letters)
print("ASCII Values of Uppercase Letters:", ascii_values_uppercase_letters)
part3 
# Function to decipher the cryptogram with a given shift
def decipher_cryptogram(cryptogram, shift):
    result = ""
    for char in cryptogram:
        if char.isalpha():
            ascii_value = ord(char)
            # Adjust the ASCII value based on the shift
            ascii_value -= shift
            # Ensure the character is within the alphabetic range
            if char.islower():
                if ascii_value < ord('a'):
                    ascii_value += 26
            else:
                if ascii_value < ord('A'):
                    ascii_value += 26
            result += chr(ascii_value)
        else:
            result += char
    return result

# Given cryptogram
cryptogram = "VZ FRYSVFU VZNGVRAG NAQN YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"


