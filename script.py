import os
import shutil


# this function transfers the src file to the dst directory
# if to_copy is true then there will be a copy of the target file
# in both the original directory and dst.
def transfer(to_copy: bool, src: str, dst: str):
    try:
        if to_copy:
            shutil.copy(src, dst)
        elif not to_copy:
            shutil.move(src, dst)
    except IsADirectoryError:
        print(to_copy, "is a directory")


# this function uses a recursive search algorithm to look through all files
# the starting directory. if the file has the desired suffex it is transferred
# to the location specified in the dest argument
def search_and_transfer(dir, suffix, to_copy, dest):
    directories = os.listdir(dir)

    for directory in directories:
        path = os.path.join(dir, directory)
        if path.endswith(suffix):
            try:
                transfer(to_copy, path, dest)
                print(directory, "transferred")
            except FileNotFoundError:
                print("file not found")
        elif os.path.isdir(path):
            try:
                search_and_transfer(path, suffix, to_copy, dest)
                print(directory, "searched")
            except PermissionError:
                print(directory, "denied access")


def main():
    message = 'Please enter the file suffix you would like transferred.\n'
    message += 'for example to move all text files enter ".txt": '
    suffix = input(message)

    message = "pelase enter the path of your destination file: "
    dest = input(message)

    if not os.path.exists(dest):
        os.makedirs(dest)

    message = 'would you like to make a copy of the file you are transfering?'
    message += '(y/n): '
    ans = input(message)
    if ans == 'y':
        copy = True
    else:
        copy = False

    message = 'please enter the path of '
    message += 'the search to start from\n'
    message += 'to search hole system enter your home directory:'

    start = input(message)

    search_and_transfer(start, suffix, copy, dest)


if __name__ == "__main__":
    main()
