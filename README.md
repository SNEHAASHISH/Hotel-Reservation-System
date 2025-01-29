# Hotel Room Reservation System

## Overview
The **Hotel Room Reservation System** is a web application designed to manage room bookings in a hotel with 97 rooms distributed across 10 floors. The system dynamically calculates the total travel time between booked rooms and optimally assigns rooms based on predefined rules. The application is built using **Flask** for the back end, **HTML/CSS** for the front end, and **JavaScript** for dynamic interactions.

---

## Key Features
1. **Room Booking**: Users can book up to 5 rooms at a time.
2. **Travel Time Calculation**: The system calculates the total travel time between the first and last room in the booking.
3. **Optimal Room Assignment**: Rooms are assigned based on the following priorities:
   - Rooms on the same floor.
   - Rooms that minimize the total travel time if not available on the same floor.
4. **Random Room Occupancy**: Users can randomize room occupancy to simulate different scenarios.
5. **Reset Booking**: Users can reset all bookings to start fresh.

---

## Backend (Flask)
The backend is implemented using **Flask**, a lightweight web framework for Python. It handles room availability, booking logic, and travel time calculation.

### Key Functions
1. **`calculate_travel_time(rooms)`**:
   - **Purpose**: Calculates the total travel time between the first and last room in the booking.
   - **Logic**:
     - Calculate the floor difference between the first and last room.
     - Calculate the room difference on the same floor.
     - Total travel time = (floor difference * 2) + room difference.

2. **`book()`**:
   - **Purpose**: Handles room booking based on the number of rooms requested.
   - **Logic**:
     - First, try to book rooms on the same floor.
     - If not enough rooms are available on the same floor, book across floors, prioritizing rooms that minimize travel time.

3. **`randomize()`**:
   - **Purpose**: Randomly books a subset of rooms to simulate occupancy.
   - **Logic**: Randomly selects a number of rooms and marks them as booked.

4. **`reset()`**:
   - **Purpose**: Resets all bookings, making all rooms available again.

---

## Frontend (HTML/CSS/JavaScript)
The frontend is built using **HTML** for structure, **CSS** for styling, and **JavaScript** for dynamic interactions with the backend.

### Key Components
1. **Room Grid**:
   - Displays rooms across all floors.
   - Rooms are color-coded to indicate availability (green for available, red for booked).

2. **Controls**:
   - **Input Field**: Allows users to specify the number of rooms to book (1-5).
   - **Book Button**: Triggers the booking process.
   - **Reset Button**: Resets all bookings.
   - **Random Button**: Randomizes room occupancy.

3. **Dynamic Rendering**:
   - The room grid is dynamically rendered based on room availability fetched from the backend.

### Key JavaScript Functions
1. **`renderRooms(rooms)`**:
   - **Purpose**: Renders the room grid based on the current availability.
   - **Logic**: Iterates through each floor and room, updating the grid to reflect availability.

2. **`fetchAvailability()`**:
   - **Purpose**: Fetches the current room availability from the backend and updates the grid.
   - **Logic**: Makes an AJAX call to the `/availability` endpoint and updates the room grid.

3. **`bookRooms()`**:
   - **Purpose**: Handles the booking process.
   - **Logic**: Validates the input, makes an AJAX call to the `/book` endpoint, and updates the grid based on the response.

4. **`resetBooking()`**:
   - **Purpose**: Resets all bookings.
   - **Logic**: Makes an AJAX call to the `/reset` endpoint and updates the grid.

5. **`randomizeRooms()`**:
   - **Purpose**: Randomizes room occupancy.
   - **Logic**: Makes an AJAX call to the `/randomize` endpoint and updates the grid.

---

## Styling (CSS)
The CSS file (`style.css`) provides the visual styling for the application, including:
- **Container Layout**: Centers the content and provides padding.
- **Room Grid**: Displays rooms in a grid format, with different styles for available and booked rooms.
- **Controls**: Styles for buttons and input fields.
- **Footer**: Contains social links and copyright information.

---

## How to Run the Application
1. **Install Dependencies**:
   - Ensure Python and Flask are installed.
   - Install Flask using `pip install flask`.

2. **Run the Application**:
   - Navigate to the project directory.
   - Run the Flask application using `python main.py`.
   - Access the application at `http://127.0.0.1:5000`.

3. **Interact with the Application**:
   - Use the input field to specify the number of rooms to book.
   - Click the "Book" button to book rooms.
   - Use the "Random" button to randomize room occupancy.
   - Use the "Reset" button to clear all bookings.

---

## Conclusion
The **Hotel Room Reservation System** is a functional web application that efficiently manages room bookings while minimizing travel time for guests. The combination of Flask for backend logic and HTML/CSS/JavaScript for frontend interactivity provides a seamless user experience. The system is designed to be easily extendable, allowing for future enhancements such as user authentication, advanced booking rules, and more.

---

## Author
- **Sneh Aashish Gupta**
- GitHub: [SNEHAASHISH](https://github.com/SNEHAASHISH)
- LinkedIn: [Sneh Aashish Gupta](https://www.linkedin.com/in/sneh-aashish-gupta/)
- Deployed Website: [Hotel Reservation System](https://sagroczz.pythonanywhere.com/)
