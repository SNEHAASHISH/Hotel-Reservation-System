from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize room availability
rooms = {
    'Floor 1': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Floor 2': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Floor 3': [301, 302, 303, 304, 305, 306, 307, 308, 309, 310],
    'Floor 4': [401, 402, 403, 404, 405, 406, 407, 408, 409, 410],
    'Floor 5': [501, 502, 503, 504, 505, 506, 507, 508, 509, 510],
    'Floor 6': [601, 602, 603, 604, 605, 606, 607, 608, 609, 610],
    'Floor 7': [701, 702, 703, 704, 705, 706, 707, 708, 709, 710],
    'Floor 8': [801, 802, 803, 804, 805, 806, 807, 808, 809, 810],
    'Floor 9': [901, 902, 903, 904, 905, 906, 907, 908, 909, 910],
    'Floor 10': [1001, 1002, 1003, 1004, 1005, 1006, 1007]
}

# Track booked rooms
booked_rooms = []


def calculate_travel_time(rooms):
    if not rooms:
        return 0
    first_room = rooms[0]
    last_room = rooms[-1]
    floor_diff = abs((first_room // 100) - (last_room // 100))
    room_diff = abs((first_room % 100) - (last_room % 100))
    return (floor_diff * 2) + room_diff


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/availability')
def availability():
    available_rooms = {room: room not in booked_rooms for floor in rooms.values() for room in floor}
    return jsonify({'available_rooms': available_rooms})


@app.route('/book', methods=['POST'])
def book():
    num_rooms = int(request.json['num_rooms'])
    available_rooms = [room for floor in rooms.values() for room in floor if room not in booked_rooms]

    if len(available_rooms) < num_rooms:
        return jsonify({'error': 'Not enough rooms available'})

    # Try to book rooms on the same floor first
    for floor, floor_rooms in rooms.items():
        floor_available = [room for room in floor_rooms if room not in booked_rooms]
        if len(floor_available) >= num_rooms:
            booked = floor_available[:num_rooms]
            booked_rooms.extend(booked)
            travel_time = calculate_travel_time(booked)
            return jsonify({'booked_rooms': booked, 'travel_time': travel_time})

    # If not enough rooms on the same floor, book across floors
    booked = available_rooms[:num_rooms]
    booked_rooms.extend(booked)
    travel_time = calculate_travel_time(booked)
    return jsonify({'booked_rooms': booked, 'travel_time': travel_time})


@app.route('/randomize', methods=['POST'])
def randomize():
    global booked_rooms
    booked_rooms = random.sample([room for floor in rooms.values() for room in floor], random.randint(1, 97))
    return jsonify({'message': 'Rooms randomized'})


@app.route('/reset', methods=['POST'])
def reset():
    global booked_rooms
    booked_rooms = []
    return jsonify({'message': 'All bookings have been reset'})


if __name__ == '__main__':
    app.run(debug=True)
