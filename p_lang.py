in_line = str(input("Enter Sentence to convert to P-Language:"))

vowels = ["a","e","i","o","u","A","E","I","O","U"]

out_line = ""
for word in in_line.split():
        for i in range(len(word)):
                if word[i] in vowels:
                        if i==0:
                                out_line += word[i] + "p" + word[i]
                                continue
                        elif i>=1:
                                if word[i] in vowels and word[i-1] in vowels:
                                        out_line += word[i]
                                        continue
                                else:
                                        out_line += word[i] + "p" + word[i]
                        else:
                                out_line += word[i]  
                else:
                        out_line += word[i]

        out_line += " "


print(out_line)
                
