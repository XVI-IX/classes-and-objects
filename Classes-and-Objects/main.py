class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):

        if not isinstance(name, str):
            raise TypeError("Name Should be a string")
        else:
            self.name = name

        if not isinstance(age, int):
            raise TypeError("Age has to be an integer")
        else:
            self.age = age

        if not isinstance(tracks, list):
            raise TypeError("Tracks must be a list")
        else:
            self.tracks = tracks

        if ((not isinstance(score, int)) & (not isinstance(score, float))):
            raise TypeError("Score has to a float or integer")
        else:
            self.score = score

    def change_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a String!!!")
        else:
            self.name = new_name

    def change_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError(f"Age must be an integer")
        else:
            self.age = new_age

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()