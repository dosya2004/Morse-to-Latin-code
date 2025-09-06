class MorseCodeConverter:
    def __init__(self):
        
        self.latin_to_morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
            '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
            ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
            '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
        }
        
     
        self.morse_to_latin = {v: k for k, v in self.latin_to_morse.items()}
    
    def encode(self, text):
        """Convert Latin text to Morse code"""
        result = []
        for char in text.upper():
            if char in self.latin_to_morse:
                result.append(self.latin_to_morse[char])
            else:
                result.append('?')  
        return ' '.join(result)
    
    def decode(self, morse_code):
        """Convert Morse code to Latin text"""
        result = []
        
        morse_chars = morse_code.split(' ')
        for morse_char in morse_chars:
            if morse_char in self.morse_to_latin:
                result.append(self.morse_to_latin[morse_char])
            else:
                result.append('?')  
        return ''.join(result)
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*40)
        print("       MORSE CODE CONVERTER")
        print("="*40)
        print("1. Encode text to Morse code")
        print("2. Decode Morse code to text")
        print("3. View Morse code chart")
        print("4. Exit")
        print("="*40)
    
    def view_chart(self):
        """Display Morse code chart"""
        print("\n" + "="*50)
        print("          MORSE CODE CHART")
        print("="*50)
        print("LETTER  MORSE     LETTER  MORSE")
        print("-"*50)
        
        
        for i in range(0, 26, 2):
            if i + 1 < 26:
                letter1 = chr(65 + i)
                letter2 = chr(66 + i)
                print(f"{letter1:6} {self.latin_to_morse[letter1]:8} {letter2:6} {self.latin_to_morse[letter2]}")
        
        print("\nNUMBERS:")
        for num in range(10):
            print(f"{num:6} {self.latin_to_morse[str(num)]}")
        
        print("\nSYMBOLS:")
        symbols = ['.', ',', '?', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@']
        for i in range(0, len(symbols), 2):
            if i + 1 < len(symbols):
                sym1 = symbols[i]
                sym2 = symbols[i + 1]
                print(f"{sym1:6} {self.latin_to_morse[sym1]:8} {sym2:6} {self.latin_to_morse[sym2]}")
    
    def run(self):
        """Main application loop"""
        print("Welcome to Morse Code Converter!")
        print("Characters not in the dictionary will be replaced with '?'")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-4): ").strip()
                
                if choice == '1':
                    text = input("Enter text to encode to Morse code: ")
                    morse_result = self.encode(text)
                    print(f"\nMorse code: {morse_result}")
                
                elif choice == '2':
                    morse_code = input("Enter Morse code to decode (separate characters with spaces): ")
                    text_result = self.decode(morse_code)
                    print(f"\nDecoded text: {text_result}")
                
                elif choice == '3':
                    self.view_chart()
                
                elif choice == '4':
                    print("Thank you for using Morse Code Converter! Goodbye!")
                    break
                
                else:
                    print("Invalid choice! Please enter 1, 2, 3, or 4.")
            
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user. Exiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")


def test_converter():
    """Test the Morse code converter with examples"""
    converter = MorseCodeConverter()
    
    
    test_cases = [
        "HELLO WORLD",
        "SOS",
        "123",
        "PYTHON IS AWESOME!",
        "TEST@EMAIL.COM"
    ]
    
    print("Testing Morse Code Converter:")
    print("-" * 30)
    
    for test_text in test_cases:
        print(f"Original: {test_text}")
        morse = converter.encode(test_text)
        print(f"Encoded: {morse}")
        decoded = converter.decode(morse)
        print(f"Decoded: {decoded}")
        print("-" * 30)


if __name__ == "__main__":
    converter = MorseCodeConverter()
    converter.run()
