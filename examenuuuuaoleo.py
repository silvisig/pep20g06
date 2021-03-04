"""
A shoe factory needs an iterable object to keep track of shoes produces by each worker each day.
Each worker has a string name and each shoe has an int serial number.
Object will have an instance variable tha will keep track of workers trying to cheat in the form of a list of names.
Iterating the object will return the serial numbers produced that day by all workers

1) 40p: Definition
    a) 5p: Class with constructor that receives the date in the format you desire
    b) 25p: Method for adding work done by worker
        - 5p: argument: 5p
            - 1 receives worker name as string
            - 2 receives series produced as list of ints
        - 10p: using this method more then once for the same worker allows the worker to add new values but not
            retransmit old values .In case existing value is entered by two workers a specific exception
            (DuplicateDataException - created by you) and inheriting ValueError will be raised.
            (ex name1: 100, 101; name1: 101, 102; results in exception DuplicateDataException) 10p
        - 10p: method validates that series introduced do not already belong to another worker. In case of conflict
            series will be removed from both workers and information will be added to instance variable that tracks
            cheating workers and then ValueError with message: "Conflict series: <series>, Workers: <nume1>, <nume2>"
            will be raised
    c) 10p: Iterating this object will return an instance of an iterator that will have all series produced that day

2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add data for the following workers:
        - Joe: 402, 403, 409
        - Ana: 399, 404, 405
        - Tim: 400, 401, 406
        - workerX: 406, 407, 408 - after adding workerX, workerX will have 407, 408 and Tim will have 400, 401
    c) 10p: Add data for Tim: 400, 401 and check that DuplicateDataException is raised
    d) 10p: Iterate the created object and save each value on a new line in a file

3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""


class ShoesIterator():
    "clasa interatorului"

    def __iter__(self):
        return self

    def __next__(self):
        if not self.serie:
            raise StopIteration
        return self.serie.pop(0)

    def __init__(self, serie):
        self.serie = serie


class DuplicatedData(ValueError):
    pass


class Shoes():

    def __init__(self, date: str):
        self.date = date
        self.workers = {}

    def _validate(self):
        for key, value in self.workers.items():
            for serial in value:
                for serii in self.series:
                    if serii == serial:
                        raise ValueError("Conflict series: " + str(serii) + " workers: " + key +" "+ self.name)
                    else:
                        print(self.series)
        return self.workers.items()

    def worker(self, name: str, series: list):
        self.name = name
        self.series = series
        self._validate()
        self.workers.update({name: series})


shoes = Shoes('13.02.2021')
shoes.worker('Joe', [402, 403, 409])
shoes.worker('Ana', [399, 404, 405])
shoes.worker('Tim', [400, 401, 406])
try:
  shoes.worker('WrokerX', [406, 407, 408])
except ValueError as whatever:
    print(whatever)

# cum faccccc sa am o instanta a iteratorului meu???
# ShoesIterator(self.series)??
def __iter__(self)->ShoesIterator:
         return ShoesIterator(self.series)


f = open("examenul.txt", "x")
for sh, serie in shoes.workers.items():
    print(sh, serie)
    f.write(str(sh) + str(serie) + "\n")
f.write("\n")
# key-numele, series-list- value
# argument
# duplicatedata
