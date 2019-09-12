class Classroom:
    classroomIDs = []
    def __init__(self, capacity, roomID):
        Classroom.classroomIDs.append(roomID)
        self.capacity = capacity
        self.roomID = roomID
        self.schedule = []

    def isFree(self, start, end):
        is_free = True
        for i in self.schedule:
            if end < i["start"] or start > i["end"]:            # (end < i["start"] and start < i["start"]) or (start > i["end"] and end > i["end"]):
                pass
            else:
                is_free = False
                break
        return is_free

    def Reserve(self, start, end):
        if (self.isFree(start, end)):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    @classmethod
    def getAvailableRooms(cls):
        return str.join(",", cls.classroomIDs)

    @staticmethod
    def isValidSlot(start, end):
        return start < end

def main():
    classroom1 = Classroom(60, "208E PAB")
    classroom2 = Classroom(30, "314W PAB")
    classroom3 = Classroom(40, "114W PAB")

    while True:
        startornot = input("Here you can reserve a classroom. Available IDs are " + Classroom.getAvailableRooms() + " Enter 'start' to start the reservation. enter 'finish' to exit")
        if startornot == "start":
            while True:
                ID = input("insert the ID of the classroom you want")
                if ID == classroom1.roomID:
                    chosenclassroom = classroom1
                    break
                elif ID == classroom2.roomID:
                    chosenclassroom = classroom2
                    break
                elif ID == classroom3.roomID:
                    chosenclassroom = classroom3
                    break
                else:
                    print("there is no classroom with such ID")

            while True:
                answer = input("Do you want to reserve a classroom")
                if answer == "yes":
                    start = (input("Please insert the starting time"))
                    end = (input("Please insert the ending time"))

                    if (Classroom.isValidSlot(start, end)):
                        if chosenclassroom.isFree(start, end) == False:
                            print("Not available for ", classroom1.roomID)
                        else:
                            chosenclassroom.Reserve(start, end)
                            print("You just reserved the classroom ", classroom1.roomID, "from", start, " to ", end)
                            print(chosenclassroom.schedule)
                    else:
                        print("The slot is invalid")
                elif answer == "no":
                    break
                else:
                    print("your answer has to be 'yes' or 'no'")
        elif startornot == "finish":
            break
        else:
            print("please follow the instructions")

main()



main()

