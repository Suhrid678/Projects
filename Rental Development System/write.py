def write_to_text(data):
    try:
        file = open("Land.txt", "w")
        for item in data:
            file.write(",".join(item) + "\n")
        print("Data written successfully ")
    except:
        print("Error:")