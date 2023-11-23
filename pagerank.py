def getCombinations(vertices):
    combinations = []
    combination = []
    for i in range(0, len(vertices)):
        for j in range(0, len(vertices)):
            combination.append(vertices[i])
            combination.append(vertices[j])
            combinations.append(combination)
            combination = []
    return combinations


def getAdjacencyValues(combinations):
    # adjacency_values = [0, 1, 1, 0, 0, 1, 1, 0, 0]
    adjacency_values = []
    for data in combinations:
        print(data)
        value = int(
            input("Enter the adjacency value between these two vertices given above: "))
        adjacency_values.append(value)
    return adjacency_values


def getLinksPresent(combinations, adjacency_values):
    present_links = []
    for i in range(0, len(adjacency_values)):
        if adjacency_values[i] == 1:
            present_links.append(combinations[i])
    return present_links


def getIncomingLinks(present_links, vertices):
    incoming_links = []
    incoming_link = []
    for i in range(0, len(vertices)):
        for j in range(0, len(present_links)):
            if vertices[i] == present_links[j][1]:
                # print(present_links[j])
                incoming_link.append(present_links[j])
                # print(incoming_link)
        incoming_links.append(incoming_link)
        incoming_link = []
    return incoming_links


def getLengthOfIncominglinks(incoming_links):
    len_of_incoming_links = []
    for data in incoming_links:
        length = len(data)
        len_of_incoming_links.append(length)
    return len_of_incoming_links


def getOutgoingLinks(present_links, vertices):
    outgoing_links = []
    outgoing_link = []
    for i in range(0, len(vertices)):
        for j in range(0, len(present_links)):
            if vertices[i] == present_links[j][0]:
                # print(present_links[j])
                outgoing_link.append(present_links[j])
                # print(outgoing_link)
        outgoing_links.append(outgoing_link)
        outgoing_link = []
    return outgoing_links


def getLengthOfOutgoinglinks(outgoing_links):
    len_of_outgoing_links = []
    for data in outgoing_links:
        length = len(data)
        len_of_outgoing_links.append(length)
    return len_of_outgoing_links


def main():
    d = 0.85
    vertices = [0, 1, 2]

    # InitialPageRank = [1, 0.575, 1]
    combinations = getCombinations(vertices)
    adjacency_values = getAdjacencyValues(combinations)
    present_links = getLinksPresent(combinations, adjacency_values)
    incoming_links = getIncomingLinks(present_links, vertices)
    len_of_incoming_links = getLengthOfIncominglinks(incoming_links)
    outgoing_links = getOutgoingLinks(present_links, vertices)
    len_of_outgoing_links = getLengthOfOutgoinglinks(outgoing_links)
    print(incoming_links)
    print(len_of_incoming_links)
    print(outgoing_links)
    print(len_of_outgoing_links)

    def brac_values(vertices, page, PageRank):
        # PageRank = [1, 0.575, 1]

        results = []
        res = []
        incoming = incoming_links[page]
        print("zxcz",incoming)
        incom_links = []
        for data in incoming:
            link = data[0]
            incom_links.append(link)

        bracs = []
        brac = []
        for link in incom_links:
            print(link)
            res = PageRank[link]/len_of_outgoing_links[link]
            brac.append(res)
        bracs.append(brac)
        brac = []

        total = sum(bracs[0])

        rank = (1 - d) + d * total
        print(rank)
        return rank

    PageRank = [1, 1, 1]
    prev = PageRank
    newPageRank = []
    for i in range(0, len(vertices)):
        value = brac_values(vertices, i, PageRank)
        newPageRank.append(value)
        PageRank = newPageRank
    print(newPageRank)
    while prev != newPageRank:
        prev = newPageRank
        newPageRank = []
        for i in range(0, len(vertices)):
            value = brac_values(vertices, i, PageRank)
            newPageRank.append(value)
            PageRank = newPageRank
        print(newPageRank)

main()
