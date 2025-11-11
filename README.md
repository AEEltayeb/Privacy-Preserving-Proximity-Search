# Privacy Preserving Proximity Search

This project is a **Django web application** demonstrating a privacy-preserving approach to location services by implementing **Proximity Search** using **Homomorphic Encryption**.

The core goal is to find the **10 nearest points of interest** to a user's location **without the server ever learning the user's exact coordinates** during the distance calculation.

---

## Core Technology

- **Paillier Homomorphic Encryption**
- Implemented via the [phe](https://github.com/n1analytics/python-paillier) Python library.

Homomorphic encryption allows the server to perform operations (addition, subtraction, multiplication) **directly on encrypted data**, enabling distance calculations **without decrypting the user's input**.

---

## Project Function Summary

The application is structured around a single Django app: `encDst` (Encrypted Destination/Distance). The sequence of operations is:

1. **Initialization:**  
   On the first visit, the database is populated with **100 random location points** (e.g., Cafe, Park, Shawarma restaurant).

2. **Input:**  
   The user enters their **x and y coordinates** into the web form (`index.html`).

3. **Key Generation:**  
   A new Paillier **Public/Private Key pair** is generated for the session.

4. **Encryption:**  
   User coordinates (x, y) are immediately encrypted using the Public Key.

5. **Encrypted Calculation (Privacy Step):**  
Enc(x_loc) - Enc(x_user) = Enc(diff_x)

This allows the coordinate difference to be computed **without revealing the user's location**.

6. **Decryption & Distance:**  
The server decrypts the differences (`diff_x`, `diff_y`) and calculates the **Euclidean distance**:

sqrt(diff_x^2 + diff_y^2)


7. **Output:**  
The results are sorted, and the **top 10 nearest activities** are displayed to the user.

---

## Installation and Usage

### Prerequisites

- Python 3.11 or later  
- pip

### Setup

1. **Extract the Archive:**  
Unzip the project files.

2. **Navigate to the Project Folder:**  
cd /path/to/coe426
3. Install Dependencies:
   pip install django phe
4. Run Migrations::
   python manage.py migrate

##Running the Application

1. Start the Server:
python manage.py runserver
2. Access the App:
Open your browser and navigate to:
http://127.0.0.1:8000/encDst/main/
The main view will automatically populate the database with 100 locations if it is empty.

Notes

The application demonstrates privacy-preserving proximity search suitable for sensitive location-based services.

All calculations on user coordinates are performed encrypted, ensuring user privacy.
