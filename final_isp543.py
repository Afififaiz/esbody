#Calculate bmi
def calc_bmi(weight, height):
  bmi = weight / ((height / 100) ** 2)
  return bmi

# Define BMI category based on BMI value
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese"
    else:
        return "Extremely Obese"


# Rule 6: Calculate BMR based on gender
# Calculate BMR for men
def calculate_bmr_for_men(weight, height, age):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    return bmr

# Calculate BMR for women
def calculate_bmr_for_women(weight, height, age):
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

 # Rule 13-17: Determine maintenance calorie based on activity level
# Calculate maintenance calorie based on activity level
def calculate_maintenance_calorie(bmr, activity_level):
    if activity_level == "Sedentary":
        return bmr * 1.2
    elif activity_level == "Lightly Active":
        return bmr * 1.375
    elif activity_level == "Moderately Active":
        return bmr * 1.55
    elif activity_level == "Very Active":
        return bmr * 1.725
    elif  activity_level == "Extremely Active":
        return bmr * 1.9
    else:
        return 0

# Calculate calorie intake suggestion based on BMI category, activity level, and goal
def calculate_calorie_intake(bmi_category, activity_level, goal, maintenance_calorie):
    
    if bmi_category in ["Underweight", "Normal"] and goal == "Bulking":
            if activity_level == "Sedentary":
                calorie_intake = maintenance_calorie + (maintenance_calorie * 0.05)
            elif activity_level == "Lightly Active":
                calorie_intake = maintenance_calorie + (maintenance_calorie * 0.09)
            elif activity_level == "Moderately Active":
                calorie_intake = maintenance_calorie + (maintenance_calorie * 0.12)
            elif activity_level == "Very Active":
                calorie_intake = maintenance_calorie + (maintenance_calorie * 0.15)
            elif activity_level == "Extremely Active":
                calorie_intake = maintenance_calorie + (maintenance_calorie * 0.18)
            else:
                calorie_intake = 0
                
    elif bmi_category in ["Normal","Overweight", "Obese", "Extremely Obese"] and goal == "Cutting":
            if activity_level == "Sedentary":
                calorie_intake = maintenance_calorie - (maintenance_calorie * 0.18)
            elif activity_level == "Lightly Active":
                calorie_intake = maintenance_calorie - (maintenance_calorie * 0.15)
            elif activity_level == "Moderately Active":
                calorie_intake = maintenance_calorie - (maintenance_calorie * 0.12)
            elif activity_level == "Very Active":
                calorie_intake = maintenance_calorie - (maintenance_calorie * 0.09)
            elif activity_level == "Extremely Active":
                calorie_intake = maintenance_calorie - (maintenance_calorie * 0.05)
            else:
                calorie_intake = 0
    return calorie_intake

#meal plan suggestion
def get_food_options(calorie_intake):
    if 1500 <= calorie_intake < 1600:
        food_options = "Vegetarian Meal Plan"
    elif 1600 <= calorie_intake < 1700:
        food_options = "Low-Carb Meal Plan"
    elif 1700 <= calorie_intake < 1800:
        food_options = "Balanced Meal Plan"
    elif 1800 <= calorie_intake < 1900:
        food_options = "High-Protein Meal Plan"
    elif 1900 <= calorie_intake < 2000:
        food_options = "Gluten-Free Meal Plan"
    elif 2000 <= calorie_intake < 2100:
        food_options = "Keto Meal Plan"
    elif 2100 <= calorie_intake < 2200:
        food_options = "Paleo Meal Plan"
    elif 2200 <= calorie_intake < 2300:
        food_options = "Vegan Meal Plan"
    elif 2300 <= calorie_intake < 2400:
        food_options = "Low-Sodium Meal Plan"
    else:
        food_options = "Customized Meal Plan"
    return food_options


# Forward chaining to determine BMI category, BMR, and maintenance calorie
def forward_chaining(age, weight, height, gender, activity_level, goal):
    if gender == "Male":
        bmr = calculate_bmr_for_men(weight, height, age)
    elif gender == "Female":
        bmr = calculate_bmr_for_women(weight, height, age)
    else:
        bmr = 0
    bmi = calc_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)
    maintenance_calorie = calculate_maintenance_calorie(bmr, activity_level)
    calorie_intake = calculate_calorie_intake(bmi_category, activity_level, goal, maintenance_calorie)
    food_options = get_food_options(calorie_intake)

    return bmi_category, bmr, maintenance_calorie, calorie_intake, food_options


def calculate_calorie_surplus(bmi_category, activity_level, goal, maintenance_calorie):
    if bmi_category in ["Underweight", "Normal"] and goal == "Bulking":
        if activity_level == "Sedentary":
            calorie_surplus = round(maintenance_calorie * 0.05)
        elif activity_level == "Lightly Active":
            calorie_surplus = round(maintenance_calorie * 0.09)
        elif activity_level == "Moderately Active":
            calorie_surplus = round(maintenance_calorie * 0.12)
        elif activity_level == "Very Active":
            calorie_surplus = round(maintenance_calorie * 0.15)
        elif activity_level == "Extremely Active":
            calorie_surplus = round(maintenance_calorie * 0.18)
        else:
            calorie_surplus = 0
    else:
        calorie_surplus = 0

    return calorie_surplus


def calculate_calorie_deficit(bmi_category, activity_level, goal, maintenance_calorie):
    if bmi_category in ["Normal", "Overweight", "Obese", "Extremely Obese"]and goal == "Cutting":
        if activity_level == "Sedentary":
            calorie_deficit = round(maintenance_calorie * 0.18)
        elif activity_level == "Lightly Active":
            calorie_deficit = round(maintenance_calorie * 0.15)
        elif activity_level == "Moderately Active":
            calorie_deficit = round(maintenance_calorie * 0.12)
        elif activity_level == "Very Active":
            calorie_deficit = round(maintenance_calorie * 0.09)
        elif activity_level == "Extremely Active":
            calorie_deficit = round(maintenance_calorie * 0.05)
        else:
            calorie_deficit = 0
    else:
        calorie_deficit = 0

    return calorie_deficit


#Using reasoning to provide recommendations
def reasoning(bmi_category, goal, weight, calorie_intake,maintenance_calorie, activity_level):
    recommendations = []

    if goal == "Bulking" and (bmi_category == "Underweight" or bmi_category == "Normal"):
        protein_intake = round(2 * weight)
        fat_intake = round(0.8 * weight)
        carbs_intake = round((calorie_intake - (2 * weight * 4) - (0.8 * weight * 9)) / 4)
        calorie_surplus = calculate_calorie_surplus(bmi_category, activity_level, goal, maintenance_calorie)
        recommendations.append(f"Aim to consume around {protein_intake} grams of protein per day.")
        recommendations.append(f"Include approximately {fat_intake} grams of fat in your daily diet.")
        recommendations.append(f"Consume about {carbs_intake} grams of carbohydrates per day.")
        recommendations.append(f"Increase a calorie surplus of {calorie_surplus} calories per day to promote weight gain.")

    elif goal == "Cutting" and bmi_category == "Normal":
        protein_intake = round(2.2 * weight)
        fat_intake = round(0.6 * weight)
        carbs_intake = round((calorie_intake - (2.2 * weight * 4) - (0.6 * weight * 9)) / 4)
        calorie_deficit = calculate_calorie_deficit(bmi_category, activity_level, goal, maintenance_calorie)
        recommendations.append(f"Aim to consume around {protein_intake} grams of protein per day.")
        recommendations.append(f"Include approximately {fat_intake} grams of fat in your daily diet.")
        recommendations.append(f"Consume about {carbs_intake} grams of carbohydrates per day.")
        recommendations.append(f"Maintain a calorie deficit of {calorie_deficit} calories per day to promote fat loss.")

    elif goal == "Cutting" and (bmi_category == "Overweight" or bmi_category == "Obese" or bmi_category == "Extremely Obese"):
        protein_intake = round(1 * weight)
        fat_intake = round(0.5 * weight)
        carbs_intake = round((calorie_intake - (1 * weight) - (0.5 * weight * 9)) / 4)
        calorie_deficit = calculate_calorie_deficit(bmi_category, activity_level, goal, maintenance_calorie)
        recommendations.append(f"Aim to consume around {protein_intake} grams of protein per day.")
        recommendations.append(f"Include approximately {fat_intake} grams of fat in your daily diet.")
        recommendations.append(f"Consume about {carbs_intake} grams of carbohydrates per day.")
        recommendations.append(f"Maintain a calorie deficit of {calorie_deficit} calories per day to promote fat loss.")

    return recommendations

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


# Function to handle button click event
def calculate_button_click():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        gender = gender_var.get()
        activity_level = float(activity_entry.get())

        if activity_level <= 0:
             activity_level = "Sedentary"
        elif activity_level == 1 or activity_level == 2:
            activity_level = "Lightly Active"
        elif activity_level == 3 or activity_level == 4:
            activity_level = "Moderately Active"
        elif activity_level == 5 or activity_level == 6:
            activity_level = "Very Active"
        elif activity_level >= 7:
            activity_level = "Extremely Active"
        
        bmi_score = round(calc_bmi(weight, height), 2)
        bmi_class = get_bmi_category(bmi_score)

        bmi_label.config(text=f"Your BMI is: {bmi_score}\nYour BMI category is: {bmi_class}")

        goal = goal_var.get()
        
        # Perform forward chaining
        bmi_category, bmr, maintenance_calorie, calorie_intake, food_options = forward_chaining(age, weight, height, gender, activity_level, goal)

        # Perform reasoning
        recommendations = reasoning(bmi_category, goal, weight, calorie_intake, maintenance_calorie, activity_level)

        # Display the results in the GUI
        result_text = "Results:\n"
        result_text += f"Activity Level: {activity_level}\n"
        result_text += f"BMR: {round(bmr, 2)}\n"
        result_text += f"Maintenance Calorie: {round(maintenance_calorie, 2)}\n"
        result_text += f"Calorie Intake: {round(calorie_intake, 2)}\n"
        result_text += f"Food Options: {food_options}\n\n"
        result_text += "Recommendations:\n"
        for recommendation in recommendations:
            result_text += f"- {recommendation}\n"
        #perform bacwkard chaining technique to find the fact based on th result    
        result_text += f"\nConclusion:\n-What can be concluded based on the recommendation is that you have selected the {goal} goal based on your BMI category of {bmi_category} and will correspond whether calorie surplus or deficit. \n-Additionally, your BMI was calculated based on your weight input of {round(weight)} kg and height input of {round(height)} cm. \n-The process allowed the system to determine the appropriate activity level {activity_level} because you input {activity_entry.get()} days of exercise per week, \n-BMR was calculated based on your {gender} gender and age of {age} years old with its respected formula with its maintenance calorie of {round(maintenance_calorie, 2)} kcal, \n-Calorie intake of {round(calorie_intake, 2)} kcal determine the meal plan of {food_options} for you.\n"    

        result_label.config(text=result_text, justify="left")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid values for age, weight, and height.")

# Create the GUI
window = tk.Tk()
window.title("Nutrition for Bodybuilding")

# Set the background color of the window
window.configure(bg="#B2FFFF")  # Pastel blue color

# Create a spacer
spacer_label = tk.Label(window, text="", bg="#B2FFFF")
spacer_label.pack()

# Create a frame to hold the age label and question button
age_frame = tk.Frame(window, bg="#B2FFFF")
age_frame.pack()

# Create the age label
age_label = tk.Label(age_frame, text="Age:", bg="#B2FFFF")
age_label.pack(side="left")

# Create a question button for age information
age_info_button = tk.Button(age_frame, text="?", bg="red", command=lambda: messagebox.showinfo("Age Information", "Please enter your age in years. The age input will be used to calculate the Basal Metabolic Rate (BMR) per person along with the gender,  that which will be subsequently input into the system."))
age_info_button.pack(side="left", padx=(5, 0))  # Adjust the padx value as needed

# Create the age entry field
age_entry = tk.Entry(window)
age_entry.pack()


# Create a frame to hold the weight label and question button
weight_frame = tk.Frame(window, bg="#B2FFFF")
weight_frame.pack()


# Create the weight label
weight_label = tk.Label(weight_frame, text="Weight (kg):", bg="#B2FFFF")
weight_label.pack(side="left")

# Create a question button for weight information
weight_info_button = tk.Button(weight_frame, text="?", bg="red", command=lambda: messagebox.showinfo("Weight Information", "Please Enter your weight in kilograms. This weight input will be used to calculate the Body Mass Index (BMI) value and category per person along with the height, that which will be subsequently input into the system"))
weight_info_button.pack(side="left", padx=(5, 0))  # Adjust the padx value as needed

# Create the weight entry field
weight_entry = tk.Entry(window)
weight_entry.pack()

# Create a frame to hold the height label and question button
height_frame = tk.Frame(window, bg="#B2FFFF")
height_frame.pack()



# Create the height label
height_label = tk.Label(height_frame, text="Height (cm):", bg="#B2FFFF")
height_label.pack(side="left")

# Create a question button for height information
height_info_button = tk.Button(height_frame, text="?", bg="red", command=lambda: messagebox.showinfo("Height Information", "Please Enter your height in centimeters. This Height input and Height input before will be used to get the BMI "))
height_info_button.pack(side="left", padx=(5, 0))  # Adjust the padx value as needed

# Create the height entry field
height_entry = tk.Entry(window)
height_entry.pack()


# Create a frame to hold the gender label and question button
gender_frame = tk.Frame(window, bg="#B2FFFF")
gender_frame.pack()

# Create the gender label
gender_label = tk.Label(gender_frame, text="Gender:", bg="#B2FFFF")
gender_label.pack(side="left")

# Create a question button for gender information
gender_info_button = tk.Button(gender_frame, text="?", bg="red", command=lambda: messagebox.showinfo("Gender Information", "Please Select your gender either Male or Female. This is crucial to calculate the BMR along with the age"))
gender_info_button.pack(side="left", padx=(5, 0))  # Adjust the padx value as needed

# Create the gender selection menu
gender_var = tk.StringVar(window)
gender_var.set("Male")
gender_options = ["Male", "Female"]
gender_menu = tk.OptionMenu(window, gender_var, *gender_options)
gender_menu.pack()


# Create a frame to hold the activity label and question button
activity_frame = tk.Frame(window, bg="#B2FFFF")
activity_frame.pack()

# Create the activity label
activity_label = tk.Label(activity_frame, text="Exercise days frequency per week:", bg="#B2FFFF")
activity_label.pack(side="left")

# Create a question button for activity level information
activity_info_button = tk.Button(activity_frame, text="?", bg="red", command=lambda: messagebox.showinfo("Exercise Information", "Please Enter your exercise frequency in a range between 1  until 7 or above 7 exercise per week. This frequency will be used to set the activity level based on the exercise"))
activity_info_button.pack(side="left", padx=(5, 0))  # Adjust the padx value as needed

# Create the activity entry field
activity_entry = tk.Entry(window)
activity_entry.pack()


# Create the BMI label
bmi_label = tk.Label(window, text="" , bg="#B2FFFF")
bmi_label.pack()


# Create a frame to hold the goal label and question button
goal_frame = tk.Frame(window, bg="#B2FFFF")
goal_frame.pack()

# Create the goal label
goal_label = tk.Label(goal_frame, text="Goal:", bg="#B2FFFF")
goal_label.pack(side="left")

# Create a question button for goal information
goal_info_button = tk.Button(goal_frame, text="?", bg="red", command=lambda: messagebox.showinfo("Goal Information", "Please Select your goal that available in the select dropdown. Only goal that available corresponding to your bmi will be displayed: \n\nIf your bmi is underweight, you can only choose goal that is bulking \n\nIf your bmi is normal, you can choose goal either bulking or cutting \n\nIf your bmi is either overweight, obese, extremely obese, you can only choose goal that is cutting"))
goal_info_button.pack(side="left", padx=(5, 0))  # Adjust the padx value as needed

# Create the goal selection
goal_var = tk.StringVar(window)
goal_var.set("Available")

def update_goal_options(*args):
    selected_bmi_category = get_bmi_category(calc_bmi(float(weight_entry.get()), float(height_entry.get())))
    if selected_bmi_category == "Underweight":
        goal_options = ["Bulking"]
    elif selected_bmi_category == "Normal":
        goal_options = ["Bulking", "Cutting"]
    elif selected_bmi_category == "Overweight" or selected_bmi_category == "Obese" or selected_bmi_category == "Extremely Obese":
        goal_options = ["Cutting"]
    else:
        goal_options = []

    goal_menu['menu'].delete(0, 'end')
    for goal in goal_options:
        goal_menu['menu'].add_command(label=goal, command=tk._setit(goal_var, goal))

goal_var.trace('w', update_goal_options)

goal_menu = tk.OptionMenu(window, goal_var, ())
goal_menu.pack()

# Create a spacer
spacer_label = tk.Label(window, text="", bg="#B2FFFF")
spacer_label.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_button_click, bg="#98FB98")
calculate_button.pack()

# Create the result label
result_label = tk.Label(window, text="", bg="#B2FFFF")
result_label.pack()

# Run the GUI
window.mainloop()

'''
1.	Introduction
Achieving a fit and muscular physique has become a common goal for many men and women in today's society. However, for those who are new to fitness, determining the right caloric intake and macronutrient balance can be a confusing and overwhelming task. It's important to determine whether one should be in a caloric surplus or deficit in order to build muscle, but this can be difficult to do without proper guidance. In addition, people often do not know what amounts of carbohydrates, proteins, and fats they should take in daily to achieve their desired body shape goals.

The importance of a balanced diet cannot be overstated, as the right balance of macronutrients is essential for both optimal muscle growth and overall health. However, despite the crucial role that diet plays in reaching fitness goals, many individuals struggle to determine the right balance for their needs. This problem is compounded by the overwhelming amount of information available online, which can often lead to confusion and misinformation.

To help these individuals overcome these challenges, it's important to provide a solution that can guide them in determining their caloric intake and macronutrient balance, and help them monitor their progress along the way. This is where our focus comes in - to create a solution that will simplify the process and make it easier for men and women to reach their fitness goals.


1.1 Problem statement 
We aim to develop an expert system to help men and women on their fitness journey. The system will focus on monitoring their calorie intake and macro-nutrient consumption, allowing individuals to track and understand the amount of macronutrients like carbohydrates, proteins, and fats they are consuming. This expert system will provide a solution to effectively manage their diet and reach their desired body shape goals, making their journey easier and more manageable.

●	The complexity of determining and designing an optimal nutrition plan such as the exact amounts of carbohydrates, proteins, and fats should be taken in daily.
●	People often do not know their suitable goal (bulking and cutting) corresponding to their bmi level.
●	People often confuse bmi and bmr.
●	People often does not know about their exact Basal Metabolic Rate based on their gender and age
●	People often does not know the true and exact amount of maintenance calorie that they need to added more  based on loss of calorie they lost based on their level of activity.

1.2 Scope 
●	The system will ask about the user's age, height, weight, and gender in order to their BMI and BMR.
●	The system will provide information about the proportion of carbohydrates, proteins, and fats consumed and help users to maintain a balanced and healthy diet.
●	The system will provide personalized recommendations based on individual goals and progress, taking into account factors such as age, gender, activity level, and weight.

1.3 Project significant
●	The system must be able to provide personalized recommendations based on individual needs and goals.
●	The user interface and overall user experience must be intuitive, easy to use, and engaging.
●	Allowing user to know how much amount of carbohydrates, proteins, and fats they are consuming.
●	Allowing user to choose if they goals fitness is to bulking or cutting if their BMI is not overweight.
●	Additional recommendation of meals that users can take based on their diet and fitness goal.





1.4 Objectives
●	To provide personalized recommendations based on individual needs and goals for calorie intake and macro-nutrient consumption.
●	To allow users to track the amount of carbohydrates, proteins, and fats they are consuming and provide recommendations for maintaining a balanced and healthy diet.
●	To provide recommendations for meals based on individual diet and fitness goals.
●	To allow users to track their progress over time and make informed decisions about their diet and fitness goals.
●	To provide reliable and accurate information based on the latest research and scientific data.

2.	Methodology for knowledge acquisition and representation
2.1	Knowledge acquisition

A crucial aspect of acquiring education is obtaining knowledge from multiple sources such as textbooks, guides, and case studies, among others. For our project, we consulted with specialists in the field through interviews. One of the interviews was with Asst. Prof. Dr Nor Azwani Bin Mohd Shukri a lecturer teaching basic medical nutrition therapy, nutrition support assessment from the International Islamic University Malaysia (UIA). We found the information gathered from this interview to be beneficial. Additionally, we researched diet and nutrition through articles on reputable websites. As a result, we developed a system that calculates the user's BMI and BMR to determine their desired fitness goal of cutting or bulking.

2.2	Variable table
Variables	Number of Values	Possible Values  
Height	1	●	Centimetre 
Weight	1	●	Kilogram 
 Gender  	2	●	Male
●	Female 
 Age 	1	●	Year 
Macros	3	●	Protein 
●	Fat 
●	Carbohydrate 
BMI	4	●	Underweight (<18.5)
●	Normal (18.5-24.9)
●	Overweight (25-29.9)
●	Obese (30-34.9)
●	Extremely obese (35>)
BMR	3	●	High
●	Medium
●	Low 
Intake	3	●	Calorie surplus
●	Calorie deficit
●	Maintenance calorie

2.3	Interview 


Question 	Answer 
1.	What does it mean by calorie intake? 	Calorie intake refers to the amount of calories consumed through food and beverages. The number of calories a person needs can vary depending on their age, gender, weight, and activity level. A calorie is a unit of measurement for energy and is often used to measure the energy content of foods. Consuming too many calories can lead to weight gain and an increased risk of health problems, while consuming too few calories can lead to weight loss and malnutrition. It's important to maintain a balance of calorie intake with energy expended.

2.	How many calories do we need to build our body? 	The number of calories needed to build the body can vary depending on an individual's age, sex, weight, height, and activity level. Generally, men need more calories than women due to their typically larger muscle mass. The recommended daily calorie intake for adult men is around 2,500 calories, while for adult women it is around 2,000 calories. However, active individuals, such as athletes or those who engage in regular intense physical activity, may require more calories to support muscle growth and repair.  

3.	How to count calorie intake? 	There are several ways to count calorie intake, including:  
●	Using a food diary: Write down everything you eat and drink throughout the day, along with the portion sizes and calorie counts. Many apps and websites can help you track your calories and provide you with a breakdown of the macronutrients (carbohydrates, protein, and fat) you are consuming. 
●	Reading nutrition labels: Most packaged foods have a nutrition label that lists the number of calories per serving. Be sure to check the serving size and adjust accordingly if you eat more or less than the recommended serving size. 
●	Consult a dietitian: if you need help counting calories, you can also talk to a dietitian. They will be able to help you figure out how many calories you should be eating each day based on your age, sex, weight, and activity level. They can also help you plan meals that are balanced and nutritious. 
It's important to note that counting calories is not the only way to maintain a healthy diet, and it's not the only factor that determines weight loss or gain. The quality of the food, eating habits, and physical activity all play a role.  

4.	How many meals per day for bodybuilders need to take? 	Bodybuilders typically eat several small meals throughout the day to help support muscle growth and repair. This is known as "meal frequency" or "eating frequency", the idea is that by eating small, frequent meals, the body is constantly supplied with the nutrients it needs to build and repair muscle tissue. The number of meals that bodybuilders need to eat per day can vary, but generally, it is recommended to eat at least 4-6 small, nutrient-dense meals per day. These meals should be high in protein, healthy fats, and complex carbohydrates to provide the body with the necessary nutrients for muscle growth and repair.  

5.	What are the best bodybuilding food? 	Bodybuilders typically focus on consuming high-protein foods, such as lean meats, fish, eggs, and dairy products, to support muscle growth and repair. Complex carbohydrates, such as brown rice, oatmeal, and quinoa, are also important for providing energy during workouts. Fruits and vegetables are also recommended for their nutrient content and antioxidant properties. Additionally, healthy fats, such as those found in nuts and avocados, can help with hormone production and cell growth. It's also important to stay hydrated by drinking enough water.  

6.	What should they eat after workout? 	After a workout, bodybuilders typically aim to consume a combination of protein and carbohydrates to support muscle recovery and replenish glycogen stores. A good post-workout meal or snack may include a source of lean protein, such as chicken, fish, or a protein shake, and a source of carbohydrates, such as sweet potatoes, brown rice, or fruit. Consuming protein and carbohydrates within 30 minutes to an hour after working out can help to improve muscle recovery and growth. Additionally, it's important to rehydrate with water or a sports drink after a workout to replace fluids lost through sweat.

7.	What should they eat before workout? 	Before working out, bodybuilders typically aim to consume a meal or snack that is high in carbohydrates and moderate in protein. Carbohydrates are important for providing energy during the workout, while protein helps to support muscle recovery and growth. A good pre-workout meal may include a source of complex carbohydrates, such as whole grains, fruit, or vegetables, and a source of lean protein, such as chicken, fish, or eggs.  

8.	Which nutrients are used for bodybuilding? 	Bodybuilding requires a balance of several key nutrients to support muscle growth, recovery, and overall health.  
Protein is essential for building and repairing muscle tissue, and can be found in a variety of foods such as lean meats, fish, eggs, and dairy products. Carbohydrates are important for providing energy during workouts and to replenish glycogen stores in the muscles. Whole grains, fruits, and vegetables are good sources of carbohydrates.  
Fats are also an important nutrient for bodybuilders, as they help to support hormone production and cell growth. Healthy fats can be found in foods such as nuts, seeds, avocados, and olive oil.  
Vitamins and minerals, such as Vitamin D, calcium, and iron are important for overall health and maintaining strong bones. Vitamin D can be obtained through sun exposure, and also can be found in fatty fish, egg yolks, and fortified milk, and calcium can be found in dairy products, leafy greens, and fortified foods. Iron can be found in red meat, poultry, beans, leafy greens, and fortified cereals.  
Additionally, bodybuilders should pay attention to their hydration, drinking enough water throughout the day to maintain proper fluid balance and support overall health.  

9.	Is body fat necessary? 	Body fat is not strictly necessary for bodybuilders, but it is important to maintain a healthy level of body fat for overall health and well-being. A certain level of body fat is necessary for the body to function properly, and too low a body fat percentage can lead to health problems such as hormonal imbalances and nutrient deficiencies.  

10.	What fats are good for bodybuilding? 	There are several types of fats that can be beneficial for bodybuilding:  
●	Monounsaturated fats: These are found in foods such as avocados, olive oil, and nuts, and can help to improve blood cholesterol levels and reduce inflammation. 
●	Polyunsaturated fats: These are found in foods such as fatty fish (salmon, sardines, mackerel), flaxseeds, and chia seeds, and can help to improve heart health and decrease inflammation in the body. 
●	Omega-3 fatty acids: These are a type of polyunsaturated fat found in fatty fish such as salmon, sardines, and mackerel, and can help to improve heart health and decrease inflammation in the body. 
●	It's important to note that while these fats can be beneficial, they should be consumed in moderation as part of a balanced diet. A diet too high in fats can lead to health problems such as obesity and heart disease. It's always best to consult a registered dietitian or a certified strength and conditioning coach to help you create a sustainable and healthy diet and workout program that's tailored to your needs and goals.  

11.	What does "eating clean" mean? 	"Eating clean" is a term that is often used in the context of bodybuilding and fitness, and refers to a type of diet that focuses on consuming whole, unprocessed foods. The idea behind eating clean is that by consuming whole foods that are free of additives and preservatives, you can better control the quality and quantity of the nutrients that you are consuming, which can help to support muscle growth and recovery. A clean eating diet typically includes a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats. It encourages to avoid processed foods, added sugars, and saturated and trans fats. The goal is to eat foods that are as close to their natural state as possible. Clean eating is often associated with a reduction in the consumption of processed foods, added sugars and saturated fats. 

12.	Why does every bodybuilders always mention about protein? 	Protein is a crucial nutrient for bodybuilders, as it is essential for building and repairing muscle tissue. When you lift weights, you create tiny tears in your muscle fibers. In order for those fibers to repair and grow, they need protein. The body uses amino acids, the building blocks of protein, to create new muscle fibers and repair existing ones. Protein is also essential for maintaining muscle mass, especially as we age. As we get older, muscle mass decreases, which can lead to a decrease in strength, mobility and overall health. Consuming adequate amounts of protein can help to slow down this process and maintain muscle mass.  

13.	How much protein does a bodybuilder need? 	The amount of protein a bodybuilder needs can vary depending on their individual needs and goals. However, generally speaking, bodybuilders typically require more protein than the average person to support muscle growth and repair. For example, a bodybuilder who weighs 80 kg would need approximately 96-160 grams of protein per day. It's important to note that this is just a general guideline and individual needs can vary depending on factors such as age, sex, activity level, and muscle mass. It's always best to consult a registered dietitian or a certified strength and conditioning coach to help you create a sustainable and healthy diet and workout program that's tailored to your needs and goals.  

14.	Is carbohydrate have anything to do with bodybuilding? 	Carbohydrates play an important role in bodybuilding as they are the primary source of fuel for the body during intense physical activity such as weightlifting. Carbohydrates are also necessary for the body to replenish glycogen stores in the muscles, which are depleted during exercise. However, the amount of carbohydrates needed will vary depending on the individual's training regimen and goals. It is important for bodybuilders to consult a nutritionist or dietitian to determine the appropriate amount of carbohydrates for their specific needs.  

Database & Knowledge Base
Database (List Of Facts)
F1: bmi is less than 18.5  
F2: bmi is underweight  
F3: bmi is 18.5 to 24.9  
F4: bmi is normal 
F5: bmi is 25 to 29.9  
F6: bmi is overweight  
F7: bmi is 30 to 34.9  
F8: bmi is obese 
F9: bmi is more than 35 
F10: bmi is extremely obese  
F11: gender is men 
F12: calculate bmr for men based on age
F13: gender is women 
F14: calculate bmr for women based on age
F15: activity level is sedentary  
F16: activity level is lightly active 
F17: activity level is moderately active  
F18: activity level is very active 
F19: activity level is extremely active 
F20: maintenance calorie is bmr * 1.2 
F21: maintenance calorie is bmr * 1.375  
F22: maintenance calorie is bmr * 1.55  
F23: maintenance calorie is bmr * 1.725 
F24: maintenance calorie is bmr * 1.9  
F25: ask what is your goal ?  
F26: goal is bulking  
F27: intake is maintenance calorie + calorie surplus 5%  
F28: intake is maintenance calorie + calorie surplus 9%  
F29: intake is maintenance calorie + calorie surplus 12%  
F30: intake is maintenance calorie + calorie surplus 15% 
F31: intake is maintenance calorie + calorie surplus 18%  
F32: goal is cutting  
F33: intake is maintenance calorie - calorie deficit 18%  


F34: intake is maintenance calorie - calorie deficit 15% 
F35: intake is maintenance calorie - calorie deficit 12%  
F36: intake is maintenance calorie - calorie deficit 9%  
F37: intake is maintenance calorie - calorie deficit 5%  
F38: protein is 2g * weight  
F39: fat is 0.8g * weight  
F40: carbs is (intake - (2g * weight * 4) - (0.8g * weight *9))/4  
F41: protein is 2.2g * weight 
F42: fat is 0.6g * weight  
F43: carbs is (intake - (2.2g * weight * 4) - (0.6g * weight *9))/4  
F44: protein is 1g * height  
F45: fat is 0.5g * weight 
F46: carbs is (intake - (1g * height) - (0.5g * weight *9))/4  
F47: calorie is more than 1500 and less than 1599 
F48: food is Vegetarian Meal Plan  
F49: calorie is more than 1600 and less than 1699  
F50: food is Low-Carb Meal Plan 
F51: calorie is more than 1700 and less than 1799  
F52: food is Balanced Meal Plan 
F53: calorie is more than 1800 and less than 1899  
F54: food is High Protein  Meal Plan 
F55: calorie is more than 1900 and less than 1999 
F56: food is Gluten Meal Plan 
F57: calorie is more than 2000 and less than 2099 
F58: food is Keto Meal Plan 
F59: calorie is more than 2100 and less than 2199 
F60: food is Paleo Meal Plan 
F61: calorie is more than 2200 and less than 2299 
F62: food is Vegan Meal Plan 
F63: calorie is more than 2300 and less than 2399  
F64: food is Low Sodium  Meal Plan 
F65: calorie is more than 2400  
F66: food is Customized Meal Plan 








Knowledge Base
BMI category 

Rule1 
if bmi is <18.5 
then bmi is underweight 
  
Rule2 
if bmi is 18.5 - 24.9 
then bmi is normal 
  
Rule3 
if bmi is 25 - 29.9 
then bmi is overweight 
  
Rule4 
if bmi is 30 - 34.9 
then bmi is obese 
  
Rule5 
if bmi is >35 
then bmi is extremely obese 
  


Calculate BMR 

Rule6 
If Men 
then calculate bmr for men based on age
  
Rule7 
If women 
then calculate bmr for women based on age


Set up activity level 

Rule8 
if little to no exercise 
then activity level is sedentary 
  
Rule9 
if exercise 1-2 days/week 
then activity level is lightly active 
  
Rule10 
if exercise 3-4 days/week 
then activity level is moderately active 
  
Rule11 
if exercise 4-5 days/week 
then activity level is very active 
  
Rule12 
if exercise 6-7 days/week or twice a day 
then activity level is extremely active 
Calculate maintenance calorie based on activity level 

Rule13 
if activity level is sedentary 
then maintenance calorie is bmr * 1.2 
  
Rule14 
if activity level is lightly active 
then maintenance calorie is bmr * 1.375 
  
Rule15 
if activity level is moderately active 
then maintenance calorie is bmr * 1.55 
  
Rule16 
if activity level is very active 
then maintenance calorie is bmr * 1.725 
  
Rule17 
if activity level is extremely active 
then maintenance calorie is bmr * 1.9 


Calorie intake suggestions based on activity level 

Rule18 
if bmi is normal 
then ask what is your goal ? 


BMI is underweight/normal, goal is Bulking 

Rule19 
if bmi is underweight 
Or bmi is normal 
And activity level is sedentary 
And goal is bulking 
then intake is maintenance calorie + calorie surplus 5% 
 
Rule20 
if bmi is underweight 
Or bmi is normal 
And activity level is lightly active 
And goal is bulking 
then intake is maintenance calorie + calorie surplus 9% 
  
Rule21 
if bmi is underweight 
Or bmi is normal 
And activity level is moderately active 
And goal is bulking 
then intake is maintenance calorie + calorie surplus 12% 
 
Rule22 
if bmi is underweight 
Or bmi is normal 
And activity level is very active 
And goal is bulking 
then intake is maintenance calorie + calorie surplus 15% 
 
Rule23 
if bmi is underweight 
Or bmi is normal 
And activity level is extremely active 
And goal is bulking 
then intake is maintenance calorie + calorie surplus 18% 


BMI is normal/overweight/obese/extremely obese, goal is Cutting 
 
Rule24 
if  bmi is normal 
Or bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
And activity level is sedentary 
And goal is cutting 
then intake is maintenance calorie - calorie deficit 18% 
 
Rule25 
if  bmi is normal 
Or bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
And activity level is lightly active 
And goal is cutting 
then intake is maintenance calorie - calorie deficit 15% 
  
Rule26 
if  bmi is normal 
Or bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
And activity level is moderately active 
And goal is cutting 
then intake is maintenance calorie - calorie deficit 12% 
  
Rule27 
if  bmi is normal 
Or bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
And activity level is very active 
And goal is cutting 
then intake is maintenance calorie - calorie deficit 9% 
 
Rule28 
if  bmi is normal 
Or bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
And activity level is extremely active 
And goal is cutting 
then intake is maintenance calorie - calorie deficit 5% 


Macro nutrition set up 
Goal is Bulking BMI is Underweight/Normal,  

Rule29 
if goal is bulking 
And bmi is underweight 
Or bmi is normal 
then protein is 2g * weight 
  
Rule30 
if goal is bulking 
And underweight 
Or bmi is normal 
then fat is 0.8g * weight 
 
Rule31 
if goal is bulking 
And underweight 
Or bmi is normal 
then carbs is (intake - (2g * weight * 4) - (0.8g * weight *9))/4 


Goal is Cutting, BMI is Normal,  

Rule32 
If goal is cutting 
And bmi is normal 
Then protein is 2.2g * weight 
 
Rule33 
If goal is cutting 
And bmi is normal 
Then fat is 0.6g * weight 
 
Rule34 
If goal is cutting  
And bmi is normal 
Then carbs is (intake - (2.2g * weight * 4) - (0.6g * weight *9))/4 


Goal is Cutting, BMI is Overweight/Obese/Extremely Obese,  

Rule35 
If goal is cutting 
And bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
Then protein is 1g * height 
 
Rule36 
If goal is cutting 
and bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
Then fat is 0.5g * weight 
 
Rule37 
If goal is cutting 
and bmi is overweight 
Or bmi is obese 
Or bmi is extremely obese 
Then carbs is (intake - (1g * height) - (0.5g * weight *9))/4 




BMI is Underweight/Normal, Activity Level is Sedentary/Lightly Active/Moderately Active/Very Active/Extremely Active, Goal is Bulking

Rule1
If bmi is underweight
Or bmi is normal
And activity level is sedentary 
And goal is bulking
Then calorie surplus is maintenance calorie * calorie surplus 5% 


Rule2
If bmi is underweight 
Or bmi is normal 
And activity level is lightly active
And goal is bulking
Then calorie surplus is maintenance calorie * calorie surplus 9% 

Rule 3
If bmi is underweight 
Or bmi is normal 
And activity level is moderately active 
And goal is bulking
Then calorie surplus is maintenance calorie * calorie surplus 12% 

Rule4
If bmi is Underweight
Or bmi is normal
And activity level is very active 
and goal is bulking 
Then calorie surplus is maintenance calorie * calorie surplus 15% 

Rule4: 
If bmi is Underweight
Or bmi is normal
And activity level is extremely active 
and goal is bulking
Then calorie surplus is maintenance calorie * calorie surplus 18% 





BMI is Normal/Overweight/Obese/Extremely Obese, Activity Level is Sedentary/Lightly Active/Moderately Active/Very Active/Extremely Active, Goal is Cutting

Rule1
If bmi is normal
Or bmi is overweight
Or bmi is obese
Or bmi is extremely obese
And activity level is sedentary 
And goal is cutting
Then calorie deficit is maintenance calorie * calorie surplus 18% 


Rule2
If bmi is normal
Or bmi is overweight
Or bmi is obese
Or bmi is extremely obese
And activity level is lightly active
And goal is cutting
Then calorie deficit is maintenance calorie * calorie surplus 15% 

Rule 3
If bmi is normal
Or bmi is overweight
Or bmi is obese
Or bmi is extremely obese
And activity level is moderately active 
And goal is cutting
Then calorie deficit is maintenance calorie * calorie surplus 12% 

Rule4
If bmi is normal
Or bmi is overweight
Or bmi is obese
Or bmi is extremely obese
And activity level is very active 
And goal is cutting 
Then calorie deficit is maintenance calorie * calorie surplus 9% 

Rule4: 
If bmi is normal
Or bmi is overweight
Or bmi is obese
Or bmi is extremely obese
And activity level is extremely active 
And goal is cutting
Then calorie deficit is maintenance calorie * calorie surplus 5% 


Determining what are the food that will be equivalent to their recommended calorie intake 

Rule39 
If calorie is more than 1500 and less than 1599 
Then food is Vegetarian Meal Plan 
 
Rule40 
If calorie is more than 1600 and less than 1699 
Then food is Low-Carb Meal Plan 
 
Rule41 
If calorie is more than 1700 and less than 1799 
Then food is Balanced Meal Plan
 
Rule42 
If calorie is more than 1800 and less than 1899 
Then food is High-Protein Meal Plan
 
Rule43 
If calorie is more than 1900 and less than 1999 
Then food is Gluten-Free Meal Plan
 
Rule44 
If calorie is more than 2000 and less than 2099 
Then food is Keto Meal Plan
 
Rule45 
If calorie is more than 2100 and less than 2199 
Then food is Paleo Meal Plan 
 
Rule46 
If calorie is more than 2200 and less than 2299 
Then food is Vegan Meal Plan
 
Rule47 
If calorie is more than 2300 and less than 2399 
Then food is Low Sodium Meal Plan 
 
Rule48 
If calorie is more than 2400 
Then food is Customized Meal Plan




'''