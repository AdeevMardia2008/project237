import os

print("\n\nMake sure there is only one file (the file you want to change) inside the folder, otherwise the rest of the files will get deleted.")

new_file_name=input("Enter the new name of the file: ")

def main():
   
    folder = input("Enter folder name: ")
    for count, filename in enumerate(os.listdir(folder)):
        new_file = f"{new_file_name}.jpg"
        source_folder =f"{folder}/{filename}"
        new_file =f"{folder}/{new_file}"
        os.rename(source_folder, new_file)
    print("\nYour file has been renamed!")
    print("\nProject 237 by Adeev Mardia\n")
 
if __name__ == '__main__':
    main()