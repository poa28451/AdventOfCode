from typing import List


def read_input_file(filename: str) -> List[str]:
    input_file = open(filename)
    lines = input_file.readlines()
    input_file.close()
    return lines


# For the first part
def checksum(filename: str):
    lines = read_input_file(filename)
    twice = 0
    thrice = 0

    for boxID in lines:
        twice_found = False  # For checking if the twice occurrence has been counted
        thrice_found = False  # For checking if the thrice occurrence has been counted

        for i in range(len(boxID)):
            if twice_found and thrice_found:  # Stop reading the current box if both cases have been found
                break

            letter = boxID[i]
            occur = boxID.count(letter)  # Count the occurrence of the current letter

            if occur == 2 and not twice_found:  # If this letter appears twice and has not been found yet
                twice += 1
                twice_found = True  # Flag the twice occurrence as found

            if occur == 3 and not thrice_found:  # If this letter appears thrice and has not been found yet
                thrice += 1
                thrice_found = True  # Flag the thrice occurrence as found

    print(twice, ' x ', thrice, ' = ', twice*thrice)


# For the second part
def checksum2(filename: str):
    lines = read_input_file(filename)

    for boxID1 in lines:
        for boxID2 in lines:
            if boxID1 == boxID2:  # Omit the same id
                break

            id_pair = zip(boxID1, boxID2)  # Pair each letter from both IDs
            common_letters = []
            differ = 0
            for letter1, letter2 in id_pair:
                if letter1 != letter2:  # If the letters differ, don't remember it
                    differ += 1
                else:
                    common_letters.append(letter1)

                if differ > 1:  # If there are more than one difference, this is not the answer
                    break

            if differ == 1:  # If there is only one difference, this is the answer
                print("".join(common_letters))


checksum2("./Day2-input.txt")
