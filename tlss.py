def tlss_func():
    import pyperclip

    def main():
        myMessage = input("Secret Text:")
        myKey = 10
        ciphertext = encryptMessage(myKey, myMessage)
        print(ciphertext + '|')
        pyperclip.copy(ciphertext)


    def encryptMessage(key, message):
        ciphertext = [''] * key

        for col in range(key):
            position = col
            while position < len(message):
                ciphertext[col] += message[position]
                position += key
        return ''.join(ciphertext)


    main()
