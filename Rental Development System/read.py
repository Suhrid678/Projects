def read_from_text():
    Gather_element = []
    try:
        file = open("Land.txt", "r")
        for i in file:
            clr = i.replace("\n", "")
            res = clr.split(",")
            Gather_element.append(res)
    except:
        print("Land database not found")
    return Gather_element