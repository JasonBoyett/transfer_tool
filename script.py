import os
import shutil


# this function transfers the src file to the dst directory
# if to_copy is true then there will be a copy of the target file
# in both the original directory and dst.
def transfer(to_copy: bool, src: str, dst: str, suffix: str):
    try:
        if to_copy:
            shutil.copy(src, dst)
        elif not to_copy:
            shutil.move(src, dst)
    except IsADirectoryError:
        search_and_transfer(src, suffix, to_copy, dst)


# this function uses a recursive search algorithm to look through all files
# the starting directory. If the file has the desired suffix it is transferred
# to the location specified in the dst argument
def search_and_transfer(dir: str, suffix: str, to_copy: bool, dst: str):
    directories = os.listdir(dir)

    for directory in directories:
        path = os.path.join(dir, directory)
        if path.endswith(suffix):
            try:
                transfer(to_copy, path, dst)
                print(directory, "transferred")
            except FileNotFoundError:
                print("file not found")
        elif os.path.isdir(path):
            try:
                search_and_transfer(path, suffix, to_copy, dst)
                print(directory, "searched")
            except PermissionError:
                print(directory, "denied access")


def get_ans() -> bool:
    message = 'would you like to make a copy of the file you are transferring?'
    message += '(y/n): '
    ans = input(message)
    if ans == 'y':
        copy = True
    else:
        copy = False
    return copy


def main():
    message = 'Please enter the file suffix you would like transferred.\n'
    message += 'for example to move all text files enter ".txt": '
    suffix = input(message)

    message = "please enter the path of your destination file: "
    dst = input(message)

    copy = get_ans()

    if not os.path.exists(dst):
        os.makedirs(dst)

    message = 'please enter the path of '
    message += 'the start of the search\n'
    message += 'to search hole system enter your home directory:'

    start = input(message)

    search_and_transfer(start, suffix, copy, dst)


if __name__ == "__main__":
    main()
