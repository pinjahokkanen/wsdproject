
<h1> <b> Online Game Store - Project Plan </b> <br/>CS-C3170 Web Software Development, 2017-2018</h1>

## **1. Team**

| **Student ID**  | **Team Member**    |
| ----------- |:-------------- |
| 476702      | Pinja Hokkanen |
| 488732      | Tatu Koivisto  |
| 526270      | Leevi Lappi    |

Our team consists of two second year students and a fourth year student, all from Information Networks major. We all have some experience on front-end development techniques and UI design, but have never worked with Django before. 

## **2. Goal**
Our first goal is to develop a well made and neat platform, that has all the mandatory requirements implemented thoroughly to ensure the basic functionalities of the service. We aim to emphasise the usability and user experience of the service, thus make it user-friendly and visually pleasing using common web design principles. Our service aims to cater the needs of our potential users and we will have a user centered approach in our business model, development and design. Since multiple displays and connectedness are important factors influencing web development, we intend to make the platform responsive and have proper social media integrations. 
	
Also, we believe that this project would be a great part to each of our personal portfolio, which is why we are ready to invest our efforts in creating a quality platform.

## **3. Features**
### 3.1 Development

Our start was slow, due to not understanding how to implement the development environment. We tried to take shortcuts with boilerplates, but these efforts were unsuccesful. Also, we realized that this was also not allowed and hence started the project from scratch. 

Our biggest development issues came from lack of project management and planning. We did not have a clear task list of features to delegate to team members. This also resulted in a lack of task schedules. We believe that this is mainly due to us not having the experience in carrying a full end-to-end software project. However, general development of the project was continuous, though used techniques and solutions were usually miscellaneous. Our development advanced in bursts. Usually, one of us was stuck on some feature issue or bug for a longer period of time until figuring a working solution. 

Our biggest **success** was persistance in creating a working entity. We believe all implemented features are well made.

We encountered major **problems** on all the features we implemented. Many times the addition of a new feature broke other parts of the system. Generally, hardest parts of development were related to working with the database, models and AJAX calls. We first tried to work with Django's generic views, but ended up in using own def views. We learned that in software development 10% of time is used to create new features and 90% of time goes to solving all the bugs the features caused. 

### 3.2 Initial Plan
We begin our project by creating few visual interpretations of our ideas to establish a common vision on how our platform should look like.  We plan to implement all the mandatory requirements as well as we possibly can to get max points from each item on the list. However, we are interested in implementing multiple additional features for our personal learning, but also to cover if mistakes happen in implementing mandatory requirements. 

Practical implementation will rely on course material, Django’s own documentation and guides found on the internet on Django. We will probably utilize external libraries and resources to increase development speed, naturally in the limitations of course learning objectives and allowance of open-source licenses.

### 3.3 Mandatory requirements **implemented**:
	
>**Authentication** 
	 - Utilization of Django Auth 
	 - Login, logout, registration
	 - Email validation using Django’s built in email back end system
	 - Password changing using Django´s built in back end

We believe our implementation of *Authentication* counts for **200 points**

>**Basic player functionalities**
	 - Buying of games, **edit order in cart**  and payment system using Niksula payments 
	 - Play games
	 - Filter games based on category
	 - Basic security restrictions

We believe our implementation of *Basic player functionalities* counts for **300 points**

>**Basic developer functionalities**
	-  Adding of games 
	-  Sales statistics and analysis tool 
	-  Security restrictions

We believe our implementation of *Basic player functionalities* counts for **175 points**

>**Game/service interaction**
	 - postMessage() methods from the game to the platform for saving
   information, such as highscores Messages from the service to the game

We believe our implementation of *Game/service interaction* counts for **200 points**

>**Quality of Work**
	 - Use of quality programming practises (DRY, refactoring, commenting)
	 - Utilization of HCI methods to develop a quality UI
	 - User experience (styling, interaction)
	 - Running tests on the service 

We believe our *Quality of Work* counts for **75 points**	 

>**Non-functional requirements**
	- Use of management methods to increase team productivity, communication and efficiency
	- Making good documentation of the project 

### 3.4  Implemented extra features

> **3rd party login:** 
> Using Django Social third party login is possible using Facebook API.
> 
We believe our implementation of *3rd party login* counts for **100 points**
> **Own game:** 
> Simple Snake game can be played on the site.  The Snake game communicates with the site using postMessage().
> 
We believe our implementation of *Snake* counts for **100 points**
> **Mobile friendly:**
> Game store is built on Bootstrap v4 and scales well for mobile devices. 
> 
We believe our implementation of *Mobile friendliness* counts for **50 points**
> **Social media sharing:** 
> Social media sharing is possible on Facebook, Google+ and Twitter. 
We believe our implementation of *Social Media Sharing* counts for **50 points**

### 3.5 Division of Work

In principle, everyone took part in making each part of the platform. Pinja's main contribution was on making the Site communicate with games and implementing the highscores service. Pinja also contributed largely to the implementation of Profiles. She also created the site's own game. Tatu's main focus was on the Profiles and its activation and password changing service. He had a huge impact on the site's visual appearance and front-end functionality (e.g. nav bar, responsivness). Leevi implemented the Store & Cart system and the Developer section of the site. He also had major impact on the site base UX and front-end functionality (e.g. single game view). This kind of division of labour allowed all to work individually and therefore it allowed asynchronous development. 

### 3.6 Model 

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

