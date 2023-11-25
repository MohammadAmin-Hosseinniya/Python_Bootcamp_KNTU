kalame = "abba"
mostavi = True

for c in range(len(kalame)):
    if kalame[c] != kalame[(c+1)*(-1)]:
        mostavi = False
        print("Thats not a palindrome.")
        break

if mostavi:
    print("Thats a palindrome.")