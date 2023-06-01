import os 
from pathlib import Path
from typing import Any
def generate_folder(Folder_name: str,File_prefix: str ,number_of_py_file: int) -> None:
    
    os.makedirs(f"{Folder_name}",exist_ok=True)
    for num in range(1,number_of_py_file+1):
        with open(f"{Folder_name}/{File_prefix}_{num}.py",mode= "w+") as f:
            pass




if __name__=="__main__":
    generate_folder("Python","Question", 10)