import re

def total_salary(name: str):
    if type(name) != str:
        return "Input data must be string"

    total = 0
    average = 0

    try:
        with open(name, "r", encoding = "utf-8") as file:
            salarys = file.readlines()
            if salarys:
                for el in salarys:
                    new_el = re.sub("\\n", "", el).split(",")
                    total += int(new_el[1])

                average = int(total / len(salarys))
                return (total, average)

            else:
                return "The specified file is empty."

    except FileNotFoundError:
        return f"Sory... file {name} not found..."

    except UnicodeDecodeError:
        return f"Sory... file {name} damaged..."

    except:
        return "Sorry... an error occurred, the file format may not match the required one."