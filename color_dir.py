import sys
from pathlib import Path
from colorama import Fore, Back, Style

def dir_ls(name: Path, my_iter: int = 0):
    spaces = None
    if my_iter == 0:
        spaces = ""
    else:
        spaces = "  " * my_iter

    if name.is_dir():
        print(f"{spaces}{Fore.BLACK}{Back.YELLOW}{name.name}{Style.RESET_ALL}")
        for el in name.iterdir():
            dir_ls(el, (my_iter + 1))
    elif name.is_file():
        print(f"{spaces}{Fore.BLUE}{name.name}{Fore.RESET}")


def main():
    if len(sys.argv) > 1:
        try:
            my_path = Path(sys.argv[1])
            if my_path.is_dir():
                dir_ls(my_path)
            else:
                print("The object at the specified path must be a directory.")

        except:
            print("Sory... some kind of error occurred. Perhaps the path you specified is incorrect.")


    else:
        print("Must be argumebt - path")

if __name__ == "__main__":
    main()