![DigitalZ logo](/images/red-logo.png)


# Welcome!


This digitalz-campaign module is a real-life example of the data analysis of the Christmas marketing campaign. Thanks to Dkiru Ltd, who kindly provided de-personalized data of their 2020 December campaign with retailers who were remotely (via mobile app) asked to perform certain business, educational or market research driven tasks. The tasks were sent each day during December month and a specific focus was on the understanding of the users' behavior:
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


[3.Technologies used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Programs Used](#programs-used)
  

[4.Testing](#testing)
  - [Flow Testing](#flow-testing)
  - [Performance Testing](#performance-testing)

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
      - *report1*: 1 loop through data:days and assigns users to the specific day. Then sorts all days:users in reverse order to find 2 days with max number of users
      - *report2*: 2 loops though data:days & data:hours, and assigns the users to different hours. Then finds the hour with max users and recommends to dispatch tasks 3 before the peak.
      - *report3*: 3 loops through data:days, area and task-type, and assigns users accordingly. Then creates dictionaries for summary of results by task-types
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

<a name="technologies-used"></a>
# 3.Technologies Used
[Go to the top](#table-of-contents)


<a name="languages-used"></a>
## Languages Used

- HTML5 

- CSS3 

- JavaScript


<a name="programs-used"></a>
## Frameworks, Libraries and Programs Used

- Balsamiq was used to create wireframes of the website (mobile-first and wide-screen versions).

- Paint.net was used to resize some of the images used.

- Font Awesome was used to import icons.

- Am I Responsive was used to generate mock-up imagery for ReadMe file.

- Chrome was used to test the source code using HTML5 and responsiveness.

- GitHub was used to create the repository and to store the project's code.

- Gitpod was used as the Code Editor for the site

- ColorHex was used to select the color-palette for the website.

- W3C Markup and Jigsaw validation tools were used to validate the HTML code and CSS style used in the project.

- JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

- Favicon-generator.org was used to create the site favicon.

- Looka was used to generate the DigitalZ logo design.

- Unsplash.com was used to choose the images for the website.



<a name="testing"></a>
# 4.Testing
[Go to the top](#table-of-contents)

The W3C Markup Validator, W3C CSS Validator and JSHint were used to validate every page, links, and  JavaScript code of the project to ensure there were no syntax errors in the project.


![W3C-html-validation](/assets/readme-assets/nu-html-checker500.jpg)
![W3C-css-validation](/assets/readme-assets/W3C-CSS-validation500.jpg)
![JShint-validation](/assets/readme-assets/jshint-test.JPG)

<a name="flow-testing"></a>
## Flow Testing
[Go to the top](#table-of-contents)

After every significant iteration, the code was tested using Chrome Developer tools and on several devices:

- Nokia8 mobile phone
- Samsung S5e tablet
- Dell XPS 13" wide (9x16) laptop 
- Samsung 24" regular (10x16) screen monitor

Each of the pages were tested for 
1. responsiveness + smooth change from vertical to horizontal layout
2. all images and texts are clear, readable and are not distorted on different screens
3. all links to other pages work 
4. accessibility (clarity of the page and next steps)
5. code executes what it supposes to
6. the flow in general 

ALL tests PASSED.


---

There were several bugs/issues with:

 - missing images and 404 error on the published website: issues related with wrong paths assignment fixed
 - responsive design including google-charts: fixed with CSS measurements and positioning manipulations
 - some functions were not executing as expected: problems fixed by changing global variables into local



<a name="performance-testing"></a>
## Performance Testing
[Go to the top](#table-of-contents)

Chrome-Developer tools-Lighthouse was performed for all pages to evaluate Performance, Accessibility, Best Practices and SEO status. No major issues found.


### Home page
### Tasks
[Go to the top](#table-of-contents)

![home-lighthouse-test](/assets/readme-assets/lighthouse-index500.jpg)
![task-lighthouse-test](/assets/readme-assets/lighthouse-guinness-task500.jpg)

### Charts
[Go to the top](#table-of-contents)

![guinness-chart-lighthouse-test](/assets/readme-assets/lighthouse-guinness-graph500.jpg)
![vitamins-chart-lighthouse-test](/assets/readme-assets/lighthouse-vitamins-graph500.jpg)



<a name="deployment"></a>
# 5.Deployment
[Go to the top](#table-of-contents)

The site was deployed to GitHub pages using the following steps:
- Sign up to GitHub
- Click on settings on the navigation bar under the repository title.
- Select pages on the left menu bar.
- Click on the master branch and save.
- The live link created by Github - https://zilvaro.github.io/digitalz-research/



<a name="acknowledgement"></a>

# 6.Acknowledgement
  [Go to the top](#table-of-contents)

- For README.md file/Deployment section, reference of github.com/josswe26/rpsls was considered.
- The code was created by developer with some theory and concepts explanations by W3C and HubSpot blog.
- The texts were created by developer with pictures sourced from unsplash.com

* Thanks to my mentor Marcel Mulders for his constructive feedback and guidance.



------