# Fitness Buddy

It is a common issue with individuals who work out that the more in shape they become, the more challenging it becomes to eat appropriately. This is because it is no longer as simple as cutting calories to lose weight; it often becomes how many calories should I consume with my current activity level to put on muscle without gaining fat? This is a very difficult balance as it is very easy to either eat too much or too little.

# Features
As a former water polo player/swimmer who is a currently active, but on a varying adult basis, my exercsise levels can change on a regular basis. I want this program to be very flexable and convenient. I want it to even allow users to guess on their data if needed (such as calories) while also having the ability to allow the user to record detailed pieces of data (such as Yogurt, 75 calroies, two servings). Then I want the program to display the information in a visual way that shows daily and weekly data. In order to do this, the program must contain the following...

- The ability to store multiple users with their own recorded information and a log in.

- Allow a user to update their information after profile is completed such as current activity level 

- Allow each specific user to know exactly how much they should eat for their current and potentially changing adult activity level. 

- Prompt the user to select their weight goals for high weight loss, moderate weight loss, maintain, grow muscle and heavy muscle gain. This must contain detailed information about what these goals mean such as heavy muscle gain often comes to increasing body fat.

- Use the Revised HBE, (Harris Benedict Equation) to calculate the users needed caloric value based off activity level.

- The ability to select and store foods to make knowing their calorie and macro values easy, so the user can select from known items and put it into their daily caloric intake. 

- Allow the user to easily understand the data/numbers with a visual (graph) that shows where they are at, and where they need to be for their activity level/ caloric intake based off their goals.

- Allow the user to record their phyiscal activities, such as swimming for one hour and then apply that to the Activity Level, the HBE and visual.


# How to Accomplish this task 
- Have the user create a profile with the following pieces of data.
    - Username
    - Password
    - Email
    - Gender
    - Height
    - Age
    - Weight
    - Daily Calories Consumed 
    - Current Activity Level
        - Define the four activity levels so the user can select what is currently approperate.
            - Sedentary
            - Mild Activity
            - Moderate Activity
            - Heavy Activity
            - Extreme Activity
    - Desired Fitness Goal 
        - Define the Caloric Goal so the user can target weight loss or muscle growth in varying degrees.
            - Extreme Weight Loss
            - High Weight Loss
            - low Weight Loss
            - Maintain
            - low Weight Groth
            - High Weight Growth
            - Extreme Weight Growth

- Allow the user to Update the infomration that is not adjusted on a daily basis such as the following information after user was created.
    - Weight
    - Caloric Goal

- Use the obtained data from the user to be applied to the Revised HBE to calculate their Current Activity Level. The users information such as gender weight and height will need to be applied to an algorithm. Information and math on the HBE can be found at https://globalrph.com/medcalcs/harris-benedict-equation-updated-basal-metabolic-rate/

- Use the obtained data from the user to be applied to the Revised HBE to calculate their caloric needs off their Desired Fitness Goal. Information can be found from the link above as well as https://www.diabetes.co.uk/bmr-calculator.html

- Prompt the user to provide a shorthand way of putting in total caloies for the day, such as "2576" while giving the option for a much more Detailed Version with a calorie caounter.
    - Detailed Version must have the ability to search for storied foods in a API.
        - User must be able to add new foods into API with the following data sets
            - Item name such as "Greek Yogurt"
            - Caloies per Serving
            - Serving Size (Text Based Description)

        - Users must be able to Edit known foods in the API. 
            - Edit Food Name
            - Edit Calories Per Serving
            - Edit Serving Size
        - Users must be able to Delete known foods
            - Remove from database

- Allow the user to enter data on their current workout of their day if they wish (not required). It must be automatically sored in an API so it can be selected again as workouts often repeat.    
    - Record the following
        - Acivity Name
        - Activity Duration
        - Calories Burned (user must provide)
    - Search data for Workout by name
        - Must display Name, duration and calories for selection into current day
- Display a data visualization on a home page for the user. Visualization should cleary show the following
    - Calories Consumed
    - Daily Calorie Goal off HBE
    - How many more of less calories were needed for Daily Goal
    - Multiple Target Caloroie Goals 


# Schedule
- Week 1 (First Half: Dec 28 - 30)
    - Create a django template for the users and app.Have very basic html laid out for more advanced work to be done.
- Week 1 (Second Half: Dec 31-03)
    - Create algorith and apply it to program to give users their results in plain text.
    - Create Visualization of data and Graph and display it for the user.
- Week 2 (First Half: Jan 04-06)
    - Create Food API as well as fitness API having it be fully functional.
    - Begin styling with CSS
- Week 2 (Second Half: Jan 07-10)
    - Polish everything: Make styling look as good and professional as possible. Search for bugs of anything that could be disruptive to the users experiance and improve.
- Week 3 (First Half: Jan 11 - 13)
    - na
- Week 3 (Second Half: Jan 14 - 17)
    - na
- Week 4 (Jan 18 - 21)
    - na
- Week 4 (Second Half: Jan 21 -)

