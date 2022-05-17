![DigitalZ logo](/images/red-logo.png)


# Welcome!


This digitalz-campaign module is a real-life example of the data analysis of the Christmas marketing campaign. Thanks to Dkiru Ltd, who kindly provided de-personalized data of their 2019 December campaign with retailers who were remotely (via mobile app) asked to perform certain business, educational or market research driven tasks. The tasks were sent each day during December month and a specific focus was on the understanding of the users' behavior:
  - when, during the month users usally are the most active
  - when, during the day, they have the time available and willingness to respond to the tasks. That would indicate to the company when to dispach new tasks
  - is there a corelation between task-types, geographical areas and the response rate

For more practical benefits to the user, each reports includes an actionable summary or insight sentence generated using the data.

Since the solution uses external GoogleSheets location to store the data and capture inputs for analysis, it can be already used 'as-is' for the data sets, imported to excel, of other months as well as to produce other related reports with a minimal change in output parameters.


The working version of the Campaign Reporting Module mobile-web pages can be found [here](https://git.heroku.com/digitalz-research.git).

![website preview](/images/am-i-responsive.jpg)





# Table of Contents

[1. General structure (flow)](#ux)
  - [1.1 Objectives](#objectives)
  - [1.2 Personas](#personas)
  -	[1.3 Color Scheme](#color-scheme)

      
[2. Features](#features)
  - [2.1 Welcome & overview](#welcome)
  - [2.2 Report # input](#report-number)
  -	[2.3 Start-date input](#start-date-input)
  - [2.4 End-date input & validation](#end-date-input)
  - [2.5 Data storage](#data-storage)
  - [2.6 Reports](#reports)
  - [2.7 Continue cycle](#another-report)


[3.Testing](#testing)
  - [3.1 Visual testing](#visual-testing)
  - [3.2 Input vlidation testing](#input-testing)
  - [3.3 PEP8 testing](#pep-testing)


[4.Fixes & improvements](#fixes-improvements)
  - [4.1 Input validation bug](#validation-code)
  - [4.2 Same-day error](#same-day)
  - [4.3 Result visualization improvement](#result-visualization)
  

[5. Deployment](#deployment)


[6. Acknowledgement](#acknowledgement)





<a name="ux"></a> 

# 1. General structure (flow)
[Go to the top](#table-of-contents)

![flow chart](/images/digitalz-reports-flowchart.png)

<a name="objectives"></a>
## 1.1 Objectives
[Go to the top](#table-of-contents)

- Allow users to explore participants' answering behavior for for different time intervals during the promo-month. 
  - This was achieved via the selection of a report and setting the start & end-date of the analysis
- Provide some insight from the data in generated reports, so the user doesn't neet to go through multiple lines to find (for example) what are the most active hours in a day and what to do with such info in practice.
  - This was achieved through adding an extra code that looks for a specific data, sorts the results and, later, constructs the line of text indicating the findings/suggestions.
- The module runs in a smooth loop to allow the user without re-starting the application to keep exploring different reports and insights.
  - This was achieved by asking (validated) question whether the user would like to continue with another report or he wants to quit for now.




<a name="personas"></a>
## 1.2 Users
[Go to the top](#table-of-contents)

**Emily** : 24 years old marketing executive responsable for the remote sales and marketing campaign. One of her objectives is to maximize the active participation of the program users and collect significant information for brand managers.

**Grace** : 39 years old Sales Strategy director who is overseeing marketing spend and wants to push sales via business tasks, but at the same maintain program fun and interesting to the retail with mixing-in the educational tasks.


<a name="color-scheme"></a>
## 1.3 Color Scheme
[Go to the top](#table-of-contents)

For the color scheme, the idea was to keep clean-white texts with highlighting some important points and drawing attention to errors or wrong inputs.

  - General text, White-normal [\033[0;37m\]. 
  - Descriptive highlight, Blue [\033[1;34m\], used in Welcome/Overview section to highlight available report types. 
  - Report highlight, Cyan [\033[1;36m\], used to draw attention to important elements in the analysis
  - Wrong input, Red [\033[1;31m\], for indicationg the Error in process where the user has to take another action. 
  - Splash text, Green [\033[1;32m\], to create a wow effect. 



<a name="features"></a>
# 2.Features
[Go to the top](#table-of-contents)


<a name="welcome"></a>
## 2.1 Welcome & overview
[Go to the top](#table-of-contents)

This is the first page you see when the app loads. On this page there is a an explanation of the data collected and the choises the user has to make going further :

![welcome-section](/images/feature-welcome.JPG) 



<a name="report-number"></a>
## 2.2 Report # input
[Go to the top](#table-of-contents)

First, user has to enter the number of the report to be executed. The valid numbers 1 to 3 are indicated and then the input is validated (validation sample is in section 2.4. "End-date input").

![report-number-input](/images/enter-report-number.JPG)


<a name="start-date-input"></a>
## 2.3 Start-date input
[Go to the top](#table-of-contents)

Then, the user is asked to enter the start-date of the period he wants to analyze. The valid input is any number between 1 & 31 (of December) (Date validation sample is in section 2.4. "End-date input")

![start-date](/images/enter-start-date.JPG) 


<a name="end-date-input"></a>
## 2.4 End-date input & validation
[Go to the top](#table-of-contents)

Finally, the user is asked to enter the end-date of the period he wants to analyze. The valid input already includes the seleted starting date and eliminates the possibility to select the end-day smaller than starting date. 

![end-date](/images/enter-end-date.JPG) 


<a name="data-storage"></a>
## 2.5 Data storage
[Go to the top](#table-of-contents)

After the user selects the report number, start and end-day of analysis, he is reminded the options he selected, 

![selected-options-display](/images/selection-display.JPG) 


and the data is recorded in GoogleSheet file for later use:

![googlesheets-record](/images/data-googlesheet-capture.JPG)


<a name="future-features"></a>
## 2.6 Reports
[Go to the top](#reports)

Each of the reports in this module has different complexity, unique features, but follows the same structure:

1.  Retrieves the data from external file
2.	Converts the data to separate elements and creates the string with specific start & end-time
3.	Runs through a different number of loops to asign other elements to the date:
      - *report1*: 1 loop through data:days and assigns users to the specific day. Then sorts all days:users in reverse order (using Lambda function) to find 2 days with max number of users
      - *report2*: 2 loops though data:days & data:hours, and assigns the users to different hours. Then, finds the hour with max users and recommends to dispatch tasks 3 before the peak.
      - *report3*: 3 loops through data:days, area and task-type, and assigns users accordingly. Then creates dictionaries for summary of results by task-types.
4.	Visualizes data for easier comprehension with a key-note or an insight

Here are some samples:

### *Report 1*

![report1](/images/report1-capture.JPG)

--

### *Report2*

![report2](/images/report2-capture.JPG)

-- 

### *Report3* 

![report3](/images/report3-capture.JPG)


<a name="end-date-input"></a>
## 2.7 Continue cycle
[Go to the top](#another-report)

Finally, the user is asked to enter Y if he wants to run a new report (differnt report or the same, just with another period). If he enters anything else that 'Y' or 'y', the cycle closes with a 'Farewell note' and a suggestion to Run Program again: 

![run-again](/images/run-again-capture.JPG) 



------

<a name="testing"></a>
# 3.Testing
[Go to the top](#table-of-contents)


<a name="visual-testing"></a>
## 3.1 Visual testing
[Go to the top](#table-of-contents)

To ensure the code produces correct reports, it was important to validate data inputs and formulas. For that purpose it was created and used a small sub-set of the real data file:

![smaller-data-sample](/images/smaller-sample.JPG) 

At each step of coding, I was running a visual test to check:
   - sets of number-values
   - date and time values
   - created variables, lists or dictionaries
   - formulas and returned data
   - typos
   - all displayed elements are visible and clear


ALL visual checks have passed to the best visual ability of examinateur.


<a name="input-testing"></a>
## 3.2 Input validation testing
[Go to the top](#table-of-contents)

To ensure that code is robust against all user input types and accepts only required values, a list of input-validation tests were performed on each input:

  - outside instructed range
  - negative number
  - empty 'Enter' click
  - letter/word 
  - end-day before start-date
  - same start-end dates
  - same dates on both ends of the proposed period

### *Example*:

![input-validation-test](/images/input-validation-test.JPG)


ALL tests PASSED.


<a name="pep-testing"></a>
## 3.3 PEP8 testing
[Go to the top](#table-of-contents)

Python was tested using PEP8 Python validator

The Python results came back with the following:

![pep8-initial](/images/problem-check-pep8-initial.JPG) 


To fix the long lines, I split them into multiple shorter lines, eliminated some verbosity. Then, after cleaning some typos and spaces, the PEP8 result was OK:

![pep8-fixed](/images/problem-check-pep8-improved.JPG)




<a name="fixes-improvements"></a>
# 4.Fixes & improvements
[Go to the top](#table-of-contents)


<a name="validation-code"></a>
## 4.1 Input validation bug
[Go to the top](#table-of-contents)

  **Issue:** Input code works well with the 'numeric' input, even outside the given range, but stops if pressed 'Enter' or input are 'letters'.

  ![validation-problem](/images/start-validation-initial.JPG) 

  **Solution:** Using loop I created a specific list-of-strings for 'legal entries' and then assigned 'Invalid input. Repeat' to everything outside that list.

### *Code before:*

![validation-code-initial](/images/input-validation-code-initial.JPG) 


### *Code after:*

![validation-code-fixed](/images/input-validation-code-improved.JPG)


<a name="same-day"></a>
## 4.2 Same-day error
[Go to the top](#table-of-contents)

  **Issue:** In report1, if you enter the same start and end days, the code gives an error message & stops.

  ![same-day-problem](/images/same-day-error.JPG) 

  **Solution:** The problem was that in the print() statement the code looks for 2 max-values in the result-string, but there is only one value (of 1 selected day). I added aditional checking if there is one or more days in the result-string and then coded 2 print() statements accordingly.

### *Code before:*

![same-day-code-before](/images/same-day-code-error.JPG) 


### *Code after:*

![same-day-code-fixed](/images/same-day-code-fix.JPG)
![same-day-fixed](/images/same-day-fix.JPG)


<a name="result-visualization"></a>
## 4.3 Result visualization improvement
[Go to the top](#table-of-contents)

  **Issue:** In report3, if you enter the same start and end days, the code gives an error message & stops.

  ![same-day-problem](/images/same-day-error.JPG) 

  **Solution:** The problem was that in the print() statement the code looks for 2 max-values in the result-string, but there is only one value (of 1 selected day). I added aditional checking if there is one or more days in the result-string and then coded 2 print() statements accordingly.

### *Code before:*

![same-day-code-before](/images/same-day-code-error.JPG) 


### *Code after:*

![same-day-code-fixed](/images/same-day-code-fix.JPG)
![same-day-fixed](/images/same-day-fix.JPG)



<a name="deployment"></a>
# 5.Deployment
[Go to the top](#table-of-contents)

The site was deployed to GitHub pages using the following steps:

1.	In Heroku account created the new app for the project
2.	Set Vars, CREDS, buildpacks (Python and node.js)
3.	In Gitpod workspace terminal:
    - Logged in to Heroku: heroku login -i 
    - Set the Heroku remote: heroku git:remote -a digitalz-research
    - Added and committed changes: git add . && git commit -m " "
    - Pushed to both GitHub and Heroku: 
      -	git push 
      -	git push heroku main

The live link created by Heroku - https://digitalz-research.herokuapp.com/



<a name="acknowledgement"></a>

# 6.Acknowledgement
  [Go to the top](#table-of-contents)

- Lucid chart -  was used to create the flow chart in the planning process for this project.
- PEP8 validator - was used to check the code was valid.
- docs.python.org, w3schools, HubSpot blog were used to clarify some theory and concepts.
- Code Institute template was used as deployment terminal
  
* Thanks to my mentor Marcel Mulders for his constructive feedback and guidance.



------