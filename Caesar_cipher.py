#the oldest and simplest encryption & decryption techniques.
#formula for encryption is (x+n)mod26 & for decryption is (x-n)mod26

alphabet='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
def encryption(plan_text,shift_key):
    cipher_text = ""
    for i in plan_text:
        if i in alphabet:
            position=alphabet.index(i)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=i
    print(f"Here is the text after encryption:{cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for i in cipher_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text+=i
    print(f"Here is the text after decryption:{plain_text}")

wanna_play=False
while not wanna_play:
   text=input("Enter the text:").lower()
   what_to_do=input("type 'encrypt' for encryption or type 'decrypt' for decryption ")
   shift=int(input("Enter the shift number :"))
   if what_to_do=="encrypt":
       encryption(plan_text=text,shift_key=shift)
   elif what_to_do=="decrypt":
       decryption(cipher_text=text,shift_key=shift)
   play_again = input("would you like to play again ? 'yes' for continue or 'no' for quit.")
   if play_again =='yes':
       wanna_play=False
   else:
       wanna_play=False
