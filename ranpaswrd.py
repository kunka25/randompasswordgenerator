import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
  """
  Generates a random password with the specified length and character types.

  Args:
    length: The length of the password.
    include_uppercase: Whether to include uppercase letters.
    include_numbers: Whether to include numbers.
    include_symbols: Whether to include symbols.

  Returns:
    A random password string.
  """
  # Define the character sets to use.
  characters = string.ascii_lowercase
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  # Generate the password.
  password = ''.join(random.sample(characters, length))

  return password

def main():
  # Get user input for length of the password.
  while True:
    try:
      password_length = int(input("Enter the desired password length (default 12): ") or 12)
      if password_length < 8:
        print("Password length should be at least 8 characters.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Get user input for character types.
  include_uppercase = input("Include uppercase letters? (y/n): ").lower() or "y"
  include_uppercase = True if include_uppercase == "y" else False

  include_numbers = input("Include numbers? (y/n): ").lower() or "y"
  include_numbers = True if include_numbers == "y" else False

  include_symbols = input("Include symbols? (y/n): ").lower() or "y"
  include_symbols = True if include_symbols == "y" else False

  # Get user input for number of passwords to generate.
  while True:
    try:
      num_passwords = int(input("Enter the number of passwords to generate (default 1): ") or 1)
      if num_passwords < 1:
        print("Number of passwords should be at least 1.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Generate and display passwords.
  for _ in range(num_passwords):
    password = generate_password(password_length, include_uppercase, include_numbers, include_symbols)
    print(password)

if __name__ == "__main__":
  main()