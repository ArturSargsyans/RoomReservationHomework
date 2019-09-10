class Classroom:

    def __init__(self, capacity, no):
        self.capacity = capacity
        self.no = no
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


def main():
    myclass = Classroom(4,5)
    print("Hello, here you can reserve a classroom")
    while True:
        start = (input("Please insert the starting time"))
        end = (input("Please insert the ending time"))

        print(start)
        if myclass.isFree(start, end) == False:
            print("Not available")
        else:
            myclass.Reserve(start, end)
            print("You just reserved the classroom from ", start, " to ", end)
            print(myclass.schedule)



main()

