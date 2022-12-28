if __name__ == "__main__":
    text = "Hello welcome to Cathay 60th year anniversary"
    new_text = text.upper().replace(" ", "")
    for i in sorted(set(new_text)):
        print(i, new_text.count(i))
