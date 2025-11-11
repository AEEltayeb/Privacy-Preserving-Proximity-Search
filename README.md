Privacy preserving Proximity Search

This project is a Django web application demonstrating a privacy preserving approach to location services by implementing Proximity Search using Homomorphic Encryption.

The core goal is to find the 10 nearest points of interest to a user's location without the server ever learning the user's exact, sensitive coordinates during the distance calculation.

-Core Technology: Paillier Homomorphic Encryption

The privacy guarantee relies on the Paillier Homomorphic Encryption scheme (implemented via the phe Python library).

Homomorphic encryption allows the server to perform mathematical operations (specifically, addition subtraction, and multiplication) directly on encrypted data. This enables the server to calculate the difference between the stored location coordinates and the user's encrypted coordinates without ever decrypting the user's input.

project Function Summary

The application is structured around a single Django app, encDst (Encrypted Destination/Distance), which performs the following sequence of operations:

Initialization: Upon the first visit, the database is populated with 100 random location points for various activities (e.g., 'Cafe', 'Park', 'Shawarma restaurant').

Input: The user enters their x and y coordinates into the web form (rendered by index.html).

Key Generation: A new Paillier Public/Private Key pair is generated for the session.

Encryption: The user's input coordinates (x,y) are immediately encrypted using the Public Key.

Encrypted Calculation (Privacy Step):

For every stored location $\mathbf{L}$, the server performs the calculation on the ciphertext:


$$\text{Enc}(\mathbf{x}_{\text{loc}}) - \text{Enc}(\mathbf{x}_{\text{user}}) = \text{Enc}(\mathbf{diff}_{\mathbf{x}})$$

This is the critical step where the coordinate difference is found without revealing $\mathbf{x}_{\text{user}}$.

Decryption & Distance: The server decrypts the differences ($\mathbf{diff}_{\mathbf{x}}, \mathbf{diff}_{\mathbf{y}}$) using the Private Key, then calculates the standard Euclidean distance ($\sqrt{\mathbf{diff}_{\mathbf{x}}^2 + \mathbf{diff}_{\mathbf{y}}^2}$).

Output: The results are sorted, and the top 10 nearest activities are displayed to the user.


Installation and Usage

1. Prerequisites

Python (3.11 or later is implied by cache files)

pip

2. Setup

Extract the Archive: Unzip the project files.

Navigate: Change directory into the folder containing manage.py.

cd /path/to/coe426


Install Dependencies: You must install Django and the Paillier Homomorphic Encryption library.

pip install django phe


Run Migrations: Initialize the database and create the Location table.

python manage.py migrate


3. Running the Application

Start the Server:

python manage.py runserver


Access the App: Open your web browser and navigate to the main input page:

$$\text{http://127.0.0.1:8000/encDst/main/}$$

(The main view will automatically populate the database with 100 locations if it's empty).
