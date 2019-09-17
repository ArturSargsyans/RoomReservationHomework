class Room:

    roomsbyID = {}
    roomsbyType = []

    def __init__(self, type, roomID, capacity):
        self.capacity = capacity
        self.roomID = roomID
        self.type = type
        Room.roomsbyID[roomID] = self
        Room.roomsbyType.append(self)

    def Print(self):
        print(self.type, self.roomID, "capacity is ", self.capacity)

    @classmethod
    def getRoomByType(cls, type):
        for room in cls.roomsbyType:
            if room.type == type:
                room.Print()

    @classmethod
    def getRoomById(cls, ID):
        if ID in cls.roomsbyID:
            return cls.roomsbyID[ID]
        print("the room cannot be found")
        return False



class Classroom(Room):
    type = "classroom"

    def __init__(self, capacity, roomID):
        super().__init__(Classroom.type, capacity, roomID)
        self.schedule = []

    def isFree(self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break

    def ReserveClassroom(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    @staticmethod
    def isValidSlot(start, end):
            return start < end



class Office(Room):
    type = "office"
    def __init__(self, capacity, roomID):
        super().__init__(Office.type, capacity, roomID)
        self.faculty = []

    def ReserveOffice(self, firstname, lastname):
        fullname = firstname + " " + lastname
        self.faculty.append(fullname)






def main():
    Classroom("314W PAB", 50)
    Classroom("208 W PAB", 30)
    Office("114W PAB", 3)
    Office("215W PAB", 2)

    print("Hello. Here are available rooms for you to reserve.\n")


    while True:
        Room.getRoomByType(Classroom.type)
        Room.getRoomByType(Office.type)
        ID = input("Enter the ID of the Room You want. Type 'exit' to exit")
        if ID in Room.roomsbyID.keys():
            currRoom = Room.getRoomById(ID)
            if currRoom.type == Classroom.type:
                while True:
                    print("The schedule for", currRoom.roomID, "\n", currRoom.schedule)
                    if input("if you want to reserve type 'go'. Type anything else to go back") == "go":
                        start = input("Please insert the starting time")
                        end = input("Please insert the ending time")

                        if Classroom.isValidSlot(start, end):
                            int(start)
                            int(end)
                            if Classroom.isFree(currRoom, start, end) == False:
                                print("not available")
                            else:
                                Classroom.ReserveClassroom(currRoom, start, end)
                        else:
                            print("invalid slot")
                    else:
                        break
            elif currRoom.type == Office.type:
                x = 0
                while x < currRoom.capacity:
                    print("The faculty of the office", currRoom.roomID, "\n", currRoom.faculty)
                    if input("if you want to reserve type 'go'. Type anything else to go back") == "go":
                        firstname = input("please insert your first name")
                        lastname = input("please insert your last name")
                        Office.ReserveOffice(currRoom, firstname, lastname)
                    else:
                        break
                if x == currRoom.capacity:
                    print("The office is full")
        elif ID == 'exit':
            break
        else:
            print("No such Room")













main()