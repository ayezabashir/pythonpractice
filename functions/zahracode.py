def name():
    nm = "Name: Ayeza Bashir\n"
    return nm + marks()

def marks():
    m = "Marks: 4/4\n"
    return  m + grade()

def grade():
    gd = "Grade: A\n"
    return gd

def main():
    report = name()
    print(report)

if __name__ == "__main__":
    main()

