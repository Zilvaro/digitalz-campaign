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
  - [1.4 Structure (Flow)](#wire-flow)
    - [Wireframes](#wireframes)
    - [Home-page](#wire-home)
    - [Tasks](#wire-tasks)
    - [Insights](#wire-charts)

      
[2. Features](#features)
  - [2.1 Sign-in & task activation](#sign-in)
  - [2.2 Tasks](#tasks)
  -	[2.3 Charts](#charts)
  - [2.4 Features-to-come (list is not complete)](#future-features)


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

- Allow users to explore relevant participants' answering behavior for for different time intervals during the promo-month. 
  - This was achieved via the selection of a report and setting the start & end-date of the analysis
- Provide some insight form the data in generated repors, so the user doesn't neet to go through multiple lines to find (for example) what are the most active hours in a day and what to do with such info in practice.
  - This was achieved through adding an extra code that looks for specific data, sorts the results and, later, constructs the line of texts indicating the findings/suggestions.
- The module runs in a smooth loop to allow the user without re-starting the application to keep exploring different reports and insights.
  - This was achieved by asking (validated) question whether the user would like to continue with another report or he wants to quit for now.

The screen-max-width is set for 1100px to keep all the items in proportion. To keep all elements visually complete and related to each other, a light background was added that is always responsive to full screen size (not only up to 1100px).



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



<a name="features"></a>
# 2.Features
[Go to the top](#table-of-contents)


<a name="sign-in"></a>
## 2.1 Sign-in & task activation
[Go to the top](#table-of-contents)

To increase site's fun (gamification), several functions were used:

1. Sign in with a name to be able to continue.  We use this name to welcome personally to the app. (In real life, I would use the name of app/user initial login instead of this place). 
2. Countdown timer. It could be done between certain dates or for a set time, but I used random time between 2 & 10 minutes for the task completion. This is used lately to get a better understanding of users’ behaviour: do they answer faster under a pressure of the short timeframe or contrary, they just drop the app? This is also will be used to relate which tasks are picked-up first under time constraints.
There is no penalty here if time expires since we still want user to do something, we just notify that allocated time has already expired. 
3. Task activation. The task is not active (clickable) if the user name was not entered. After the submission, ‘click’ icons with a link appear on the task sections. 
4. 'Breadcrumbs' on some internal pages with more related content (i.e. name of the task).


DigitalZ logo from each page always returns a user to the home-page.

![responsive home page](/assets/readme-assets/responsive-home450.webp) 
![signed-in home page](/assets/readme-assets/home-page-signed-mobile.webp) 
![expired-time home page](/assets/readme-assets/home-page-expired-mobile.webp) 


<a name="tasks"></a>
## 2.2 Tasks
[Go to the top](#table-of-contents)

Tasks section is asking the user for an opinion, insight about the brand, the market or tests his/her knowledge, for example, about training materials or working policies. It usually has rigid structure:

   - header-line that names the task (and/or topic, a company, a brand)
   - photo, reflecting the purpose or content of the text
   - task description-instructions
   - task questions that require number/radio/text input and could be supported by corresponding images
   - Submit button


![task-guinness](/assets/readme-assets/responsive-guinness-task500.jpg) 
![task-vitamins](/assets/readme-assets/responsive-vitamin-task500.jpg)


<a name="charts"></a>
## 2.3 Charts
[Go to the top](#table-of-contents)

Chart pages provide graphical representation on the Task topic. Normally, that would use the real answers, generated by multiple users, and compared with the base (average, specific market data or target). In this particular app since there is no database storage and structure, random numbers with set different intervals are generated and visualized using google-graphs.

To continue user-journey through the tasks execution, the user has 2 action options: to go to another task or exit the section.


![chart-guinness](/assets/readme-assets/responsive-guinness-chart.JPG) 
![chart-vitamins](/assets/readme-assets/responsive-vitamin-chart.JPG)
![chart-vitamins](/assets/readme-assets/exit-screen600.jpg)


<a name="future-features"></a>
## 2.4 Features-to-come (list is not complete)
[Go to the top](#table-of-contents)

Those features could be used to enhance user experience and collect more behavioral data in the future while integrating the Tasking Module into bigger solutions.

1.  Countdown timer for each task
2.	Notifications on the certain % of time elapsed
3.	Reward and status points included
4.	More information about other participants’ responses 
5.  Sharing: to allow user to share tasks with friends 


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