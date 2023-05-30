from random import randint


class SenderID:
    counter = 0
    id = {}
    max_len = 128

    @staticmethod
    def get():
        return SenderID.counter

    @staticmethod
    def reset():
        SenderID.counter = 0
        SenderID.id.clear()

    @staticmethod
    def len():
        return len(SenderID.id)

    @staticmethod
    def createID(name, phone):
        if SenderID.len() >= SenderID.max_len:
            # remove te first element of the dictionary
            SenderID.id.popitem()

        if SenderID.id.get(name+phone) is None:
            # create a new entry in the dictionary and increment the counter
            SenderID.id[name+phone] = randint(1000, 10000)
            SenderID.counter += 1

        # return the sender id from the dictionary
        return SenderID.id[name+phone]

    @staticmethod
    def removeID(name, phone):
        # remove the entry from the dictionary if it exists
        if SenderID.id.get(name+phone) is not None:
            SenderID.id.pop(name+phone)


if __name__ =='__main__':
    SenderID.max_len = 5
    id = SenderID.createID("Irfan", "12234", "a1")
    print(id, SenderID.len())
    id = SenderID.createID("Irfan", "12234", "a1")
    print(id, SenderID.len())
    id = SenderID.createID("Irfan", "12234", "a2")
    print(id, SenderID.len())
    id = SenderID.createID("Irfan", "12234657", "a1")
    print(id, SenderID.len())
    SenderID.removeID("Irfan", "12234657", "a1")
    print(SenderID.len())
    id = SenderID.createID("Irfan", "1223465", "a1")
    print(id, SenderID.len())
    id = SenderID.createID("Irfan", "1223457", "a1")
    print(id, SenderID.len())
    id = SenderID.createID("Irfan", "1234657", "a1")
    print(id, SenderID.len())
    id = SenderID.createID("Irfan", "1223467", "a1")
    print(id, SenderID.len())
    id = SenderID.createID("Irfan", "1234657", "a1")
    print(id, SenderID.len())

