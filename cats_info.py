import re

def get_cats_info(name: str):
    if type(name) != str:
        return "Input data must be string"

    cats = []

    try:
        with open(name, "r", encoding = "utf-8") as file:
            my_cats = file.readlines()
            if my_cats:
                for el in my_cats:
                    new_el = re.sub("\\n", "", el).split(",")
                    cats.append({"id": new_el[0], "name": new_el[1], "age": new_el[2]})

                return cats

            else:
                return "The specified file is empty."

    except FileNotFoundError:
        return f"Sory... file {name} not found..."

    except UnicodeDecodeError:
        return f"Sory... file {name} damaged..."

    except:
        return "Sorry... an error occurred, the file format may not match the required one."