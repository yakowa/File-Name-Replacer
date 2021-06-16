import os

usr = input('Please enter a directory on this computer in which you want all files containing a space in their name to be replaced with a hyphen.\n>>> ')

try:
    filenames = os.listdir(usr)

    for filename in filenames:
        os.rename(os.path.join(usr, filename), os.path.join(usr, filename.replace(' ', '-')))
    print(f"Successfully renamed file names in {usr}")

except:
    print(f"An Error occurred whilst trying to replacing file names in {usr}")