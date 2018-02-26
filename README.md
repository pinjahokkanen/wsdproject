
<h1> <b> Online Game Store - Final Submission & Project Plan </b> <br/>CS-C3170 Web Software Development, 2017-2018</h1>

## **1. Team**

| **Student ID**  | **Team Member**    |
| ----------- |:-------------- |
| 476702      | Pinja Hokkanen |
| 488732      | Tatu Koivisto  |
| 526270      | Leevi Lappi    |

Our team consists of two second year students and a fourth year student, all from Information Networks major. We all have some experience on front-end development techniques and UI design, but have never worked with Django before.

## **FINAL SUBMISSION**
Heroku url: http://protected-hamlet-88117.herokuapp.com/
Test users (since signing up requires confirming email, and link comes to heroku log):
	1. 	Username: test_developer
			Password: testdeveloper

	2. 	Username: test_player
			Password: testplayer

NOTE: Due to misunderstanding the instructions, we tried to fetch an initialized django-heroku project. We soon realised this was not allowed in this course, deleted all the files and started creating django project and heroku from a scratch, but the old commits from the fetched project still show up in the gitlab. After deleting the project files in the beginning we haven't looked or copied them.

### Development

In the very begin, we started with a good and ambitious attitude, and tried our best to plan the project as well as we could.
Still the actual implementation started slowly, since we had practically no deeper understanding of django environment, it's structure and connections. We tried to take shortcuts with initialized heroku-django projects, but quickly realised that this was not a good viewpont and importantly, not allowed in the course limits. Due to this our gitlab has commits from another project witch we fetched, but also deleted eventually and started the project from a scratch.

Our biggest development issues came from lack of project management and planning, even though we though we had everything quite clearly planned in the beginning. At the start, we had only bigger areas of responsibilty divided to the team members,  but not a clear task list of features. In addition to confusion between delegation, this also resulted in a lack of task schedules. We believe that this is mainly due to us not having the experience in carrying a full end-to-end software project. We had planned to use Trello as a project management platform, but instead used Telegram very actively. An approx amount of messages in our group is at least 5000 (there is no easy way to get the exact amount).
However, general development of the project was continuous, though used techniques and solutions were usually miscellaneous. Our development advanced in bursts. Usually, one of us was stuck on some feature issue or bug for a longer period of time until figuring a working solution, and after a review with other team members we usually could unravel the problem quickly. Also the end of the project was very intense, we both created new functionalities and reconstructed and improved old ones.

Our biggest **success** was persistance in creating a working entity, and not making any quick-fix solutions. We believe all implemented features are very well made. One great success for each of us was the journey - how to build a software from scratch with busy people, how important communications and work labour is, and also a really comprehensive understanding of MVC - platforms.

We encountered **problems** on all the features we implemented, and most of them were major. Many times the addition of a new feature broke other parts of the system. Generally, hardest parts of development were related to working with the database, models, AJAX calls and User authentication. We first tried to work with Django's generic views, but ended up using own def views on many parts. We learned that in software development 10% of time is used to create new features and 90% of time goes to solving all the bugs the features caused. In retrospective, we should have implemented test cases at early point of the development - now we just tested everything manually after each major update. Test cases would have made updating and finding the cause of problems more efficient.

### Mandatory requirements **implemented features listed**:

>**Authentication** (100-200p)
	 - Utilization of Django Auth
	 - Login, logout, registration
	 - Email validation using Django’s built in email back end system
	 - Changing the user & profile model data.

We believe our implementation of *Authentication* counts for **200 points**

>**Basic player functionalities** (100 - 300p)
	 - Buying of games, **edit order in cart**  and payment system using Niksula payments
	 - Play games
	 - Filter games based on category
	 - Basic security restrictions

We believe our implementation of *Basic player functionalities* counts for **280 points** /300,  since due to our limited understanding of security features there might be some security failures which we haven't even thought of, even though we tested and implemented everythig we had knowledge of.

>**Basic developer functionalities** 100-200 points
	-  Adding, modifying and removing of games
	-  Game inventory & Sales statistics
	-  Security restrictions

We believe our implementation of *Basic developer functionalities* counts for **180 points** / 200, since due to our limited understanding of security features there might be some security failures which we haven't thought of, even though we tested and implemented everythig we had knowledge of.

>**Game/service interaction**
	 - postMessage() methods from the game to the platform for saving
   information, such as highscores and gamestates
	 - Messages from the service to the game

We believe our implementation of *Game/service interaction* counts for **200 points**

>**Quality of Work**
	 - Use of quality programming practises (DRY, MVT, refactoring, commenting)
	 - Utilization of HCI methods to develop a quality UI
	 - User experience (styling, interaction)
	 - Running tests on the service

We believe our *Quality of Work* counts for **70 points**	/ 100, since we didn't implement test cases early during the project, and instead tested everything manually (which consumed our time)

>**Non-functional requirements**
	- Use of management methods to increase team productivity, communication and efficiency
	- Making good documentation of the project

We believe our *Non-functional requirements* counts for **170 points**	/ 200, since we should have utilized a project management platform instead of just using telegram (due to information structure and overload in telegram). We are happy to show our telegram logs if course staff requires.

### Implemented extra features

>**Save/load and resolution feature**
>The service supports saving and loading for games with the simple message protocol described in Game Developer Information

We believe our implementation of *Save/load and resolution feature* counts for **100 points**

> **3rd party login:**
> Using Django Social third party login is possible using Facebook API.

We believe our implementation of *3rd party login* counts for **100 points**

> **Own game:**
> Simple Snake game can be played on the site.  The Snake game communicates with the site using postMessage(). Supports highscore and saving gamestate perfectly, and loading gamestate when game is running (snake is moving)

We believe our implementation of *Snake* counts for **75 points**

> **Mobile friendly:**
> Game store is built on Bootstrap v4 and scales well for mobile devices.

We believe our implementation of *Mobile friendliness* counts for **50 points**

> **Social media sharing:**
> Social media sharing is possible on Facebook, Google+ and Twitter.

We believe our implementation of *Social Media Sharing* counts for **25 points** / 50, since we have succesfully declared metadata and tested it when login redirects had not been made. After login redirect, FB fetches metadat from login site, which is a problem we realized at the very end and didn't have time to fix.

**IN TOTAL OUR ESTIMATE OF THE POINTS IS 1450**

### Division of Work

In principle, everyone took part in making each part of the platform. At start, Pinja contributed in creating the models and rethinking their connections. Her main contribution was on creating the game - service interaction (including highscores, gamestates and categories) and fixing some major problems (adding developer to the game in view, changing profile information). She also created the site's own game, social media tags and was responsible of Heroku. Tatu's main focus was on authentication, extending User model and Profiles and its activation and email validation. He had a huge impact on the site's visual appearance and front-end functionality (e.g. nav bar, responsivness). Leevi implemented the paying system (and extended it with a cart system) and the Developer section of the site (adding games), and also on some security restrictions (permissions). He also had major impact on the site base UX and front-end functionality (e.g. single game view).

This kind of division of labour allowed all to work individually and therefore it allowed asynchronous development.

## **PROJECT PLAN**

We begin our project by creating few visual interpretations of our ideas to establish a common vision on how our platform should look like.  We plan to implement all the mandatory requirements as well as we possibly can to get max points from each item on the list. However, we are interested in implementing multiple additional features for our personal learning, but also to cover if mistakes happen in implementing mandatory requirements.

Practical implementation will rely on course material, Django’s own documentation and guides found on the internet on Django. We will probably utilize external libraries and resources to increase development speed, naturally in the limitations of course learning objectives and allowance of open-source licenses.

### 3.1 Mandatory requirements to be implemented:

>**Authentication**
	 - Utilization of Django Auth
	 - Login, logout, registration
	 - Email validation using Django’s built in email back end system

>**Basic player functionalities**
	 - Buying of games and payment system using Niksula payments
	 - Play games
	 - Basic security restrictions

>**Basic developer functionalities**
	- Adding of games
	-  Sales statistics and analysis tool
	-  Security restrictions

>**Game/service interaction**
	 - postMessage() methods from the game to the platform for saving
   information, such as highscores Messages from the service to the game

>**Quality of Work**
	 - Use of quality programming practises (DRY, refactoring, commenting)
	 - Utilization of HCI methods to develop a quality UI
	 - Running tests on the service

>**Non-functional requirements**
	- Use of management methods to increase team productivity, communication and efficiency
	- Making good documentation of the project

### 3.2  Additional features

> **3rd party login:**
> We aim to integrate and enable logins from other
> services. Implementation will rely on Google’s and Facebook’s own API
> guidelines and best practices.
>
> **RESTful API:**
> We want to investigate is this something we can
> implement. We do not have experience to implement this, so this will
> most likely be the module that requires most research on the team’s
> behalf.
>
> **Own game:**
> We all have experience in coding simple Javascript games,
> and therefore we are eager to develop our own game to the platform. We
> have plans to make the game a showcase of our platforms capabilities.
> A possible shortcut to take could be the use of Phaser library so we
> would not have to create our own game engine.
>
> **Mobile friendly:**
> Responsive web design will be our main design
> principle, so this feature will emerge as a side product of our work.
> Implementation relies heavily on the experience that team members have
> from designing websites and lessons learned on course ‘CS-C1180 -
> Verkkojulkaisemisen perusteet’.
>
> **Social media sharing:**
> Like the the third party login we aim to
> implement game sharing on social media for advertising games as online
> advertising is currently a major channel to increase sales. Like 3rd
> party login, the implementation will rely on social media sites’ API
> guidelines.



### 3.3 Priorities

We will have two main priorities when developing the service. First, we will focus on the mandatory requirements and basic functionalities, since everything else is built on that. Even great extra features will not compensate insufficient basic functionality of the service. Second, we’ll focus on the usability of our platform. Competition has a big effect on the current market situation, and our team believes that superior user experience leads to a greater market share. After we have ensured that these priorities have been addressed and fill both mandatory and our requirements, we will implement additional features.

### 3.4 Initial Draft of Models

## **2. Goal**
Our first goal is to develop a well made and neat platform, that has all the mandatory requirements implemented thoroughly to ensure the basic functionalities of the service. We aim to emphasise the usability and user experience of the service, thus make it user-friendly and visually pleasing using common web design principles. Our service aims to cater the needs of our potential users and we will have a user centered approach in our business model, development and design. Since multiple displays and connectedness are important factors influencing web development, we intend to make the platform responsive and have proper social media integrations.

Also, we believe that this project would be a great part to each of our personal portfolio, which is why we are ready to invest our efforts in creating a quality platform.

## **3. Plans**

We begin our project by creating few visual interpretations of our ideas to establish a common vision on how our platform should look like.  We plan to implement all the mandatory requirements as well as we possibly can to get max points from each item on the list. However, we are interested in implementing multiple additional features for our personal learning, but also to cover if mistakes happen in implementing mandatory requirements.

Practical implementation will rely on course material, Django’s own documentation and guides found on the internet on Django. We will probably utilize external libraries and resources to increase development speed, naturally in the limitations of course learning objectives and allowance of open-source licenses.

### 3.1 Mandatory requirements to be implemented:

>**Authentication**
	 - Utilization of Django Auth
	 - Login, logout, registration
	 - Email validation using Django’s built in email back end system

>**Basic player functionalities**
	 - Buying of games and payment system using Niksula payments
	 - Play games
	 - Basic security restrictions

>**Basic developer functionalities**
	- Adding of games
	-  Sales statistics and analysis tool
	-  Security restrictions

>**Game/service interaction**
	 - postMessage() methods from the game to the platform for saving
   information, such as highscores Messages from the service to the game

>**Quality of Work**
	 - Use of quality programming practises (DRY, refactoring, commenting)
	 - Utilization of HCI methods to develop a quality UI
	 - Running tests on the service

>**Non-functional requirements**
	- Use of management methods to increase team productivity, communication and efficiency
	- Making good documentation of the project

### 3.2  Additional features

> **3rd party login:**
> We aim to integrate and enable logins from other
> services. Implementation will rely on Google’s and Facebook’s own API
> guidelines and best practices.
>
> **RESTful API:**
> We want to investigate is this something we can
> implement. We do not have experience to implement this, so this will
> most likely be the module that requires most research on the team’s
> behalf.
>
> **Own game:**
> We all have experience in coding simple Javascript games,
> and therefore we are eager to develop our own game to the platform. We
> have plans to make the game a showcase of our platforms capabilities.
> A possible shortcut to take could be the use of Phaser library so we
> would not have to create our own game engine.
>
> **Mobile friendly:**
> Responsive web design will be our main design
> principle, so this feature will emerge as a side product of our work.
> Implementation relies heavily on the experience that team members have
> from designing websites and lessons learned on course ‘CS-C1180 -
> Verkkojulkaisemisen perusteet’.
>
> **Social media sharing:**
> Like the the third party login we aim to
> implement game sharing on social media for advertising games as online
> advertising is currently a major channel to increase sales. Like 3rd
> party login, the implementation will rely on social media sites’ API
> guidelines.

### 3.3 Priorities

We will have two main priorities when developing the service. First, we will focus on the mandatory requirements and basic functionalities, since everything else is built on that. Even great extra features will not compensate insufficient basic functionality of the service. Second, we’ll focus on the usability of our platform. Competition has a big effect on the current market situation, and our team believes that superior user experience leads to a greater market share. After we have ensured that these priorities have been addressed and fill both mandatory and our requirements, we will implement additional features.

### 3.4 Initial Draft of Models


![MODELS](https://lh6.googleusercontent.com/F3_drMVUkObKQfPNquZcMsPJ4Q5f-MQsvFOKQ-rfKiyNJYSTEQu0osS5jwPr2MNCsrFlEWNiR6SjmCzaBR5G=w1920-h925)

We are still considering if we one more mode: Sales, as well as if we need the Game-objects at User model.  

## **4. Process and Time Schedule**

We will proceed in our development process by dividing the project into clearly defined parts that are relevant at the current time and state of the platform. Each of the team members can then independently work on those parts to ensure the continuous development. Due to the time constraints of the team members, we will communicate mainly using digital channels. We will also try to meet face-to-face when necessary, preferably once a week, to discuss the current status of the development, new features and how those should be implemented and the labour of work together.

## 4.1 Communication channels

We will use **Telegram** as a main channel for communication and **Git** as secondary in addition to the **ad-hoc meetings** when necessary. This kind of remote communication requires a well managed project, which is why we plan to utilize Kanban methods and Trello with Kanban Flow - service as an example.

## 4.2 Schedule

We have created a rough schedule for the development and more strict deadlines for important milestones, but since we also want our process to be agile, we are aware and ready for possible adjustments and changes.

**Preweeks 1-3 (wk 50-52):** We will decide the goals, priorities and efforts regarding the project and the platform itself. We will also have a preliminary plan on which features to implement and how, but these plans can possibly change when the team members gain more insight on the actual implementation, tools and frameworks. This is done both face-to-face and by using other communication channels. A project plan will be written according to the previously mentioned preliminary plans. We will create visual interpretations which focus on the user experience and visually pleasing design. This is to ensure both that our team members reach an agreement and gain more insight of the actual platform, and to perceive the important features from the visual version. These sketches will be iterated over the time. We will do research regarding the frameworks and possible features to perceive better how they should be implemented when we start the actual development.

**Week 1:** We will arrange a meeting to go over the visual interpretations, research and structure of the platform, and set up the Kanban Flow - service for effective management. In the Kanban we will divide the development into relevant parts (e.g. features) regarding the mandatory requirements, and assign each team member with areas they are responsible of. Those additional features that we find very relevant to implement straight away will be done with the mandatory requirements.

**Week 2 - 4:** We will implement the platform according to the structure and work division determined during week 1. Progress is communicated to other team members, and assignments can be changed according to the situation.

**Week 5:**  We will finish with the mandatory requirements for the platform, and do some testing on the implemented features. We will re-evaluate the platform according to our priorities and decide on changes to the already implemented parts and additional features.

*DL First version of the platform (fulfilling mandatory requirements) done by 31.1.*

**Week 5 - 6:** We will implement the additional features, squash bugs and test the system rigorously


## **5. Testing**

We work using lean principles and test continuously parts we have built. The service platform does not seem to be too big for running tests manually.


## **6. Risk Analysis**

Biggest risks in our work comes from the limitation of time. Our team member’s have multiple commitments to work, school projects and extra activities. This can lead to a situation where work accumulates faster than final deadline’s approach.

Therefore, we aim to counter this risk by agreeing to minimal amount of work per week that every member must commit to. This way the project advances constantly and approach of deadline becomes more manageable.
