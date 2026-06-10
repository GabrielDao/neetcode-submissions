def concatenate(s1: str, s2: str) -> str:

    total_char = len(s1 + s2)
    
    if total_char > 10:
        #print("Too long!")
        return ("Too long!")
    
    else:
        #print(s1 + s2)
        return (s1 + s2)




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
