import json
import re
import pickle

class User:
    value_list : set
    name : str

    def __init__(self, u_name) -> None:
        self.name = u_name
        self.value_list = set()

class Container:
    curent_user : User

    def __init__(self, user_name) -> None:
        self.curent_user = User(user_name)
    
    def add(self,value : tuple) -> None:
            for val_el in value:
                self.curent_user.value_list.add(val_el)
    
    def remuve(self,value : tuple) -> None:
        for val_el in value:
            try:
                self.curent_user.value_list.remove(val_el)
            except:
                None

    def list(self) -> None:
        if(len(self.curent_user.value_list)):
            print(f"user {self.curent_user.name} : {self.curent_user.value_list}")
        else:
            print("No such elements")

    def find(self, value : tuple):
         
        count = 0
        res = set()

        for val_el in value:
            for list_el in self.curent_user.value_list:
                if(val_el == list_el): 
                    count += 1
                    res.add(list_el)
        
        if(count):
            print(f"List contain {count} word : {res}")
        else:
            print("No such elements")

    def grep(self, reg) -> None:
        res = set()
        for word in self.curent_user.value_list:
            res_match = re.search(rf"{reg}",word)
            if(res_match):
                res.add(word)
        if(len(res)):
            print(res)
        else:
            print("No such elements")

    def save(self) -> None:
        with open(f'{self.curent_user.name}.pkl', 'wb+') as my_file:
            pickle.dump(self.curent_user.value_list, my_file)
        print("Save completed")
        
    
    def load(self) -> None:
        try:
            with open(f'{self.curent_user.name}.pkl', 'rb+') as my_file:
                self.curent_user.value_list.update(pickle.load(my_file))
                print("Load completed")
        except:
            print("Nothing to load")
            self.curent_user.value_list = set()

    def switch(self, u_name) -> None:
        if(self.curent_user):
            print(f"now you user {self.curent_user.name}")
            
            validator = 1

            while(validator):
                get = input("Do y want to save your db? Y/N : ")
                if(get == "Y"):
                    validator = 0
                    self.save()
                elif(get == "N"):
                    validator = 0
                    print("OK")
                else:
                    print("wrong Input")

            self.curent_user.value_list.clear()
            self.curent_user.name = u_name
        else:
            self.curent_user.value_list.clear()
            self.curent_user.name = u_name

        validator = 1

        while(validator):
            get = input("Do y want to load your db? Y/N : ")
            if(get == "Y"):
                validator = 0
                self.load()
            elif(get == "N"):
                validator = 0
                print("OK")
            else:
                print("wrong Input")
    

    

    
