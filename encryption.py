

class Algorithm:

    def __init__(self): 
        pass

    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def encryption(self, plaintext):
        ciphertext = ''

        for i in range(len(plaintext)):
            text = plaintext[i]
            
            if text not in self.uppercase_letters and text not in self.lowercase_letters and text not in self.numbers: 
                raise Exception ("Not valid input") 
            
            elif text in self.uppercase_letters:
                index = self.uppercase_letters.index(text)

                if index % 2 == 0:
                    cipher_letter = self.uppercase_letters[index+1]
                    #Letter = one forward
                
                else:
                    cipher_letter = self.uppercase_letters[index-1]
                    #Letter = one back

                ciphertext += cipher_letter

            elif text in self.lowercase_letters:
                index = self.lowercase_letters.index(text)

                if index % 2 == 0: 
                    cipher_letter = self.lowercase_letters[index+1]
                    #Letter = one forward
                
                else:
                    cipher_letter = self.lowercase_letters[index-1]
                    #Letter = one back

                ciphertext += cipher_letter

            else: 
                index = self.numbers.index(text)

                if index % 2 == 0: 
                    cipher_letter = self.numbers[index+1]
                    #Letter = one forward
                
                else:
                    cipher_letter = self.numbers[index-1]
                    #Letter = one back

                ciphertext += cipher_letter

        return ciphertext 
        

    def decryption(self, ciphertext): 
        original_text = ''

        for i in range(len(ciphertext)):
            text = ciphertext[i]

            #no need to check for special characters as that check is done when the input is encrypted
            
            if text in self.uppercase_letters:
                index = self.uppercase_letters.index(text)

                if index % 2 == 0:
                    original_letter = self.uppercase_letters[index+1] 
        
                else:
                    original_letter = self.uppercase_letters[index-1] 

                original_text += original_letter 

            elif text in self.lowercase_letters:
                index = self.lowercase_letters.index(text)

                if index % 2 == 0: 
                    original_letter = self.lowercase_letters[index+1] 
                
                else:
                    original_letter = self.lowercase_letters[index-1] 

                original_text += original_letter 

            else: #plaintext[i] is in numbers
                index = self.numbers.index(text)

                if index % 2 == 0: 
                    original_letter = self.numbers[index+1] 
                
                else:
                    original_letter = self.numbers[index-1] 

                original_text += original_letter 

        return original_text 


def main():
    variable = 'Computer123'
    example = Algorithm()
    print('Text to be encrypted: ' + variable)
    encrypted = example.encryption(variable)
    print('Encrypted text: ' + encrypted)
    decrypted = example.decryption(encrypted)
    print('Decrypted text: ' + decrypted)

main()