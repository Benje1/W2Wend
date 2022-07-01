from textwrap import indent


class KaraokeBar:
    def __init__(self, _name, _num_of_rooms):
        self.name = _name
        self.num_of_rooms = _num_of_rooms
        self.room = []
        self.guests_in_bar = []

    def add_room(self, room):
        self.room.append(room)

    # def room_guest_check_in(self, guest):
    #     index = 0
    #     for room in self.room:
    #         if len(room.list_of_guests) < room.max_capacity:
    #                 room.check_guest_in(guest)
    #         else:
    #             index += 1

    def room_guest_check_in(self, guest):
        self.guests_in_bar.append(guest)
        for room in self.room:
            if len(room.list_of_guests) < room.max_capacity:
                room.check_guest_in(guest)
                self.guests_in_bar.remove(guest)

