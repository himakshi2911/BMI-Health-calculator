### BMI-Health-calculator
VITyarthi flipped course project -Nov 2025

### Overview of the Project  
A simple, efficient, and fully functional Body Mass Index (BMI) calculator built using Python. The program runs in the terminal/console and asks the user to input their weight (in kilograms) and height (in centimeters or meters). It calculates the BMI using the standard formula and displays the result along with the appropriate health category.

**Formula Used:**  
BMI = weight (kg) ÷ (height in meters)²

### Features  
- User-friendly console interface  
- Supports height input in cm or meters  
- Accurate calculation with 2 decimal places  
- Clear BMI category classification  
- Input validation (no zero/negative values)  
- Displays BMI reference table  
- Fully commented and structured code  
- Works on Windows, Mac, and Linux  
- No external libraries required  

### Technologies/Tools Used  
- **Python 3.x**  
- Standard Python libraries only (no pip install needed)  
- Any Python IDE or terminal (IDLE, VS Code, Thonny, etc.)


### Steps to Install & Run the Project  
1. Install Python from https://python.org (if not already installed)  
2. Open Notepad or any text editor  
3. Copy the above code  
4. Save the file as `bmi_calculator.py`  
5. Double-click the file OR  
   Right-click → Open with → Python  
   OR open terminal/command prompt and run:  
   ```bash
   python bmi_calculator.py
   ```


### Instructions for testing

1. **Test 1 – Normal Weight**  
   - Run the program  
   - Enter weight: 65  
   - Enter height: 170  
   **Expected Result:** BMI should be approximately 22.49 and category should be "Normal Weight"

2. **Test 2 – Underweight**  
   - Run the program  
   - Enter weight: 45  
   - Enter height: 170  
   **Expected Result:** BMI ≈ 15.57 and category should be "Underweight"

3. **Test 3 – Overweight**  
   - Run the program  
   - Enter weight: 85  
   - Enter height: 170  
   **Expected Result:** BMI ≈ 29.41 and category should be "Overweight"

4. **Test 4 – Obesity**  
   - Run the program  
   - Enter weight: 100  
   - Enter height: 165  
   **Expected Result:** BMI ≈ 36.73 and category should be "Obesity"


5. **Test 5 – Decimal Values**  
   - Run the program  
   - Enter weight: 72.5  
   - Enter height: 172.5  
   **Expected Result:** BMI ≈ 24.39 and category should be "Normal Weight"

6. **Test 6 – Very Tall Person**  
   - Run the program  
   - Enter weight: 70  
   - Enter height: 200  
   **Expected Result:** BMI = 17.5 and category should be "Underweight"

7. **Test 7 – Very Short Person**  
   - Run the program  
   - Enter weight: 60  
   - Enter height: 140  
   **Expected Result:** BMI ≈ 30.61 and category should be "Obesity"


**Result of Testing**  
All the above 10 test cases were performed on 21 Nov 2025 on vscode.  
All test cases passed successfully.  <img width="1487" height="938" alt="Screenshot 2025-11-22 125553" src="https://github.com/user-attachments/assets/7feffc46-f9b4-4e1d-9df1-80e9a7594fdb" />
<img width="1480" height="952" alt="Screenshot 2025-11-22 125504" src="https://github.com/user-attachments/assets/b10393cb-14d0-4300-ac01-594cf40163f0" />
<img width="1467" height="943" alt="Screenshot 2025-11-22 125330" src="https://github.com/user-attachments/assets/7e6fa6da-69d6-4056-b122-70fa27a5e25e" />
<img width="1393" height="930" alt="Screenshot 2025-11-22 125038" src="https://github.com/user-attachments/assets/17b475cb-ea30-4c38-b6fb-f311670825c2" />
<img width="1325" height="958" alt="Screenshot 2025-11-22 124950" src="https://github.com/user-attachments/assets/5b2b6f7b-2fc6-4935-8c14-eb4e69162f2e" />
<img width="1401" height="921" alt="Screenshot 2025-11-22 124822" src="https://github.com/user-attachments/assets/07c163b0-13d1-45db-ab8c-864ca69b0786" />
<img width="1491" height="957" alt="Screenshot 2025-11-22 124716" src="https://github.com/user-attachments/assets/ecbc20c9-8161-4b07-a9ce-98f5903a4083" />
