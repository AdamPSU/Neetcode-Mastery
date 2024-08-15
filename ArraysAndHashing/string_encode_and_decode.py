def encode(strs: list) -> str:
    for i in range(len(strs)):
        strs[i] = f"{len(strs[i])}#{strs[i]}"

    return "".join(strs)

def decode(s: str) -> list:
    strs = []

    for i in range(0, len(s), int[s[i]]):
        char_length = int(s[i])
        word = s[i:i+char_length+1]

        strs.append(word)

    return strs

enc = encode(["neet","code","love","you"])
dec = decode(enc)

print(dec)
