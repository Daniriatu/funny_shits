import csv


def main():
    verb_list = get_conjug_list("Subjuntivo", "Presente")
    print(verb_list)

def get_conjug_list(mood, tense):
    word_list = []
    with open("assets/jehle_verb_database.csv") as file:
        res = csv.DictReader(file)
        for row in res:
            if row["mood"] == mood and row["tense"] == tense:
                for i in range(3):
                    word_list.append(row[f"form_{i + 1}s"])
                    word_list.append(row[f"form_{i + 1}p"])
    return word_list
                

if __name__ == "__main__":
    main()