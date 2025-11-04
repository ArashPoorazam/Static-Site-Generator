from textnode import TextNode, TextType

def main():
    test_A = TextNode("salam", "Bold")
    test_B = TextNode("salam", "Bold")
    test_C = TextNode("slm", "Bold")

    print(test_A == test_B)
    print(test_B == test_C)

    print(test_A)







if __name__ == "__main__":
    main()