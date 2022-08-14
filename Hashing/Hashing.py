class HashMap:

    def __init__(self, max_size=10):
        self.__max_size = max_size
        self.__values = [[] for i in range(self.__max_size)]
        self.__size = 0

    def __len__(self):
        return self.__size

    def __setitem__(self, key, value):
        _hash = self.__get_hash(key)
        value = tuple([key, value])
        idx = 0
        for item in self.__values[_hash]:
            if item[0] == key:
                self.__values[_hash][idx] = value
                break
            idx += 1
        else:
            self.__values[_hash].append(value)
        self.__size += 1

    def __getitem__(self, key):
        _hash = self.__get_hash(key)
        for item in self.__values[_hash]:
            if key == item[0]:
                return item[1]

    def __delitem__(self, key):
        _hash = self.__get_hash(key)
        idx = 0
        for item in self.__values[_hash]:
            if key == item[0]:
                del self.__values[_hash][idx]
                self.__size -= 1
                return item[1]
            idx += 1

    def __get_hash(self, key):
        _hash = 0
        for char in key:
            _hash += ord(char)
        return _hash % self.__max_size

    def keys(self):
        for items in self.__values:
            if not items:
                continue
            for item in items:
                yield item[0]

    def values(self):
        for items in self.__values:
            if not items:
                continue
            for item in items:
                yield item[1]


if __name__ == '__main__':
    hashMap = HashMap()
    hashMap['march 6'] = 160
    hashMap['march 17'] = 200
    hashMap['march 1'] = 130
    hashMap['dec 10'] = 120
    print(len(hashMap))
    del hashMap['march 6']
    print(len(hashMap))
    print(list(hashMap.values()))
