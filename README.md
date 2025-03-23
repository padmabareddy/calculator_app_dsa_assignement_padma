Circle Calculator Extension  
This repository extends the original calculator application with functionality to calculate the perimeter and area of a circle based on a given radius.  
Features  
•	Basic arithmetic calculator (addition, subtraction, multiplication, division)  
•	Circle calculator that computes: (with input as radius)  
Details of scripts and html files  
The Circle Calculator extension consists of:  
•	A dedicated Circle class in circle.py module and provides two main methods:  
o	calculate_perimeter() - Calculates the perimeter using the formula: 2πr  
o	calculate_area() - Calculates the area using the formula: πr²  
•	HTML template for the circle.html interface  
•	Unit test that verify the circle calculations test using test_circle.py  
Project Structure  
calculator_app/  
├── flask_app.py                  # Main Flask application  
├── helper.py               # Helper functions for basic calculator  
├── circle.py               # helper for Circle class implementation  
├── test_circle.py          # Unit tests for Circle class  
├── static/  
│   └── main.css            # Stylesheet for the application  
└── templates/  
    ├── layout.html         # Base template with navigation  
    ├── home.html           # Homepage template  
    ├── calculator.html     # Basic calculator template  
    └── circle.html         # Circle calculator template  
How to Run the Application  
1.	Clone the repository:
Copy
git clone https://github.com/[username]/calculator_app_dsa_assignement_padma.git
cd calculator_app_dsa_assignement_padma
2.	Set up a virtual environment (recommended)
3.	Run the application
4.	Visit http://127.0.0.1:5000/ in your web browser – Navigate to Circle Calculator or General Calculator provide input radius and check the results (perimeter and area)
Unit test
Execute the unit test with: python -m unittest test_circle.py

