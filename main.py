class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
        else:
            self.name = None

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[number] = name

    def delete_contact(self, number):
        if number in self.contacts:
            del self.contacts[number]

    def find_contact(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return None

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    phone_book = PhoneBook()
    result = []
    for query in queries:
        if query.type == 'add':
            phone_book.add_contact(query.name, query.number)
        elif query.type == 'del':
            phone_book.delete_contact(query.number)
        elif query.type == 'find':
            name = phone_book.find_contact(query.number)
            if name is not None:
                result.append(name)
            else:
                result.append('not found')
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
