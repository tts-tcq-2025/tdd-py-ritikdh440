from calculator import add

if __name__ == "__main__":
    print(add(""))            # 0
    print(add("1"))           # 1
    print(add("1,2"))         # 3
    print(add("1\n2,3"))      # 6
    print(add("//;\n1;2;3"))  # 6
