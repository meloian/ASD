import sys
import time

class Node:
    # node initialization
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # doublyLinkedList initialization
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # method to append data at the end of the list
        new_node = Node(data)
        if not self.head:  # if list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    # method to process words through the modify_function
    def process_words(self, modify_function):
        if not self.head:
            print("Список порожній.")
            return
        first_word = self.head.data
        current = self.head.next
        while current:
            if current.data != first_word:
                print(f"{modify_function(current.data)}")
            current = current.next
            
    # making the list iterable
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class UserInterface:
    # method for data input with validation and retry option
    @staticmethod
    def input_data():
        while True:
            data = input("Введіть текст: ").strip()
            if not data:
                print("Помилка: Пусте введення.")
                if UserInterface.ask_retry():
                    continue
                else:
                    return None, False
            if not UserInterface.validate_data(data):
                print("Помилка: Введені дані не відповідають вимогам. Спробуйте ще раз. ")
                if UserInterface.ask_retry():
                    continue
                else:
                    return None, False
            return data.strip(".").split(), True

    # method for input validation
    @staticmethod
    def validate_data(data):
        return data.replace(".", "").replace(" ", "").isalpha()

    # method to print user instructions
    @staticmethod
    def print_instructions():
        print(
           "Інструкції: Введіть слова, розділені пробілами. В кінці дозволяється ставити крапку.\n"
           "Всі символи в словах мають бути літерами; цифри, спеціальні символи, або знаки пунктуації (крім крапки в кінці) не дозволяються."
        )
    
    # method to ask user if they want to retry input
    @staticmethod
    def ask_retry():
        retry = input("Спробувати знову? (так/ні): ").lower()
        return retry in ["так", "yes"]

def modify_word(word):
    # function to modify word as per given logic
    modified_word = word.replace('a', 'e')
    if len(modified_word) % 2 == 0:
        modified_word = modified_word[0] * 2 + modified_word[1:]
    else:
        modified_word = modified_word[:-1]
    return modified_word

def print_modified_words_with_list(words):
    # function to print modified words except the first word in the list
    if not words:
        print("Помилка: Список слів порожній.")
        return
    first_word = words[0]
    for word in words[1:]:
        if word != first_word:
            print(f"{modify_word(word)}")

def main():
    UserInterface.print_instructions()
    words_list, input_valid = UserInterface.input_data()
    if words_list and input_valid:
        start_time = time.time()
        list_memory_usage = sys.getsizeof(words_list) + sum(sys.getsizeof(word) for word in words_list)
        print("Динамічний масив:")
        print_modified_words_with_list(words_list)
        array_processing_time = time.time() - start_time
        print(f"Час виконання (масив): {array_processing_time} секунд.")
        print(f"Об’єм пам’яті (масив): {list_memory_usage} байтів.")

        start_time = time.time()
        dll = DoublyLinkedList()
        for word in words_list:
            dll.append(word)
        dll_memory_usage = sys.getsizeof(dll) + sum(sys.getsizeof(node) + sys.getsizeof(node.data) for node in dll)
        print("\nДвозв'язний список:")
        dll.process_words(modify_word)
        list_processing_time = time.time() - start_time
        print(f"Час виконання (список): {list_processing_time} секунд.")
        print(f"Об’єм пам’яті (список): {dll_memory_usage} байтів.")
    else:
        print("Обробка даних не відбулась через невідповідність умовам введення.")

if __name__ == "__main__":
    main()    





