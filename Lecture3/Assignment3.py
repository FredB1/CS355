# Queens College
# Internet And Web Technologies (CSCI 355)
# Winter 2024
# Assignment #3 - Front End Technologies
# Frederick Burke
# I did this assignment along with the class
import OutputUtil as ou


def read_file(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        states = [line.strip().split(",") for line in lines]
        return states[0], states[1:]


def main():
    title = "Frederick Burke's US States"
    alignments = ["l", "l", "l", "r"]
    types = ["S", "S", "S", "N"]
    output = "assignment3.html"
    headers, states = read_file('USStates.csv')
    for i in range(len(states)):
        name = states[i][0]
        if name == "New York":
            wiki_name = 'New_York_(state)'
        else:
            wiki_name = name
        href = "https://www.wikipedia.org/wiki/" + wiki_name.replace(' ', '_')
        a_attributes = 'href="' + href + '" target="_blank"'
        states[i][0]  = ou.create_element(ou.TAG_A, name, a_attributes)
    ou.write_html_file(output, title, headers, types, alignments, states, True)


if __name__ == '__main__':
    main()
