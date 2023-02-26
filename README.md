<h1 align="center">The Home Learning Hub</h1>

<img src="static/images/responsive.png" width="auto">

## Index - Table of Contents

*  [Purpose](#purpose)
*  [User Experience](#user-experience)
*  [Features](#features)
*  [Design](#design)
*  [Technologies Used](#technologies-used)
*  [Testing](#testing)
*  [Deployment](#deployment)
*  [Credits](#credits)

# Purpose

Working in schools, during the Covid19 pandemic, gave me a unique insight into the challenges that teachers, parents and pupils all faced with regards to remote learning. Whilst many companies were quick to meet the demands of schools, many of these products were focussed on satisfying larger audiences and were rarely bespoke for each individual school and their needs. These websites offered libraries of generic resources, but lacked a sense of community, professional dialogue, and the ability to rapidly change the resources on offer to suit pupils' needs. 

With the Home Learning Hub, my goal has been to create an online learning platform which serves as a 'hub' for the school, parents and (as an extension) pupils of a specific school. It was clear from recent years that the profession has needed to rapidly adapt and re-evaluate how we can positivly affect change in pupil's lives, and that the process of 'home-learning' should not only be resigned to extreme circumstances, but instead be used as an on-going tool. My goal would be for The Home Learning Hub to not only support the education of pupils but also: enhance pupil wellbeing, provide efficient communication betwen school and home, boost parent confidence, and continue to instil a sense of 'school community'.


# User Experience

## Objectives of the Project:

1. To produce the **MVP** (minimum viable product), that allows `users` (parents) to interact with `admins` (school administration) by booking consultation appointments and accessing a 'resource library' populated by the child's school.
2. To enable `users` to access the booking process and the resource library with ease and without the requirement of supplying credentials.
3. To allow `admins` to register and access authorised areas of the site - including the ability to manage appointments and upload resources to the library.



## Target Audience

The main target audiences for the site are `school administrators` (who can provide access to teachers) and `parents`. The website needed to be functional for both of these user groups and their different needs.

### Parents (users) needs:
- **Simple design** - focussing on being a welcoming space whilst not detracting from the main purpose of the site.
- **Accessibility** - simple navigation, supported by minimal user steps to accomplish goals.
- **Communication** - clear and present feedback to reassure the user of their actions and success with achieving goals.

### School administraion (admins) needs:
- **Unique Access** - authorisation present to open up restricted pages dedicated to managing data and admin privaleges.
- **Functionality** - the managing of appointments and the uploading of resources needs to be simple, quick and fit-for-purpose.
- **Defensive Measures** - any edits or deletions are met with additional checks to ensure data is not accidentally altered.

## Functionality Requirements

### Unauthorised (`User`) Access

| User Story Link | Requirement |
| ------------- | -------- |
| [#1](https://github.com/NickdevC/Home-Learning-Hub/issues/1#issue-1562209793) | I am able to easily recongise and understand the purpose of the site from the immediate information on the landing page |
| [#2](https://github.com/NickdevC/Home-Learning-Hub/issues/1#issue-1562209793) | I am able to easily navigate across the site, following clear signposting and using the minimal amount of clicks |
| [#3](https://github.com/NickdevC/Home-Learning-Hub/issues/1#issue-1562209793) | I am able to identify clear branding and consistency in design, providing me with confidence in site's purpose |
| [#4](https://github.com/NickdevC/Home-Learning-Hub/issues/6#issue-1562266464) | I am able to quickly and efficiently book an appointment with my child's teacher |
| [#5](https://github.com/NickdevC/Home-Learning-Hub/issues/24#issue-1587496408) | I receive confirmation feedback when submitting the appointment form to ensure my confidence in it's delivery |
| [#5](https://github.com/NickdevC/Home-Learning-Hub/issues/29#issue-1599713517) | I am challenged when inputing incorrect information into the appointment form and are given clear directions on how to remedy the fault |
| [#6](https://github.com/NickdevC/Home-Learning-Hub/issues/11#issue-1562295415) | I can access a 'resources library', displaying free resources to support my child's learning |
| [#7](https://github.com/NickdevC/Home-Learning-Hub/issues/34#issue-1599961263) | I can download a resource and have the file open as a pdf file in a seperate tab |


### Authorised (`Admin`) Access

#### Note regarding security: 
*Schools will have strict GDPR regulations in place to ensure the sharing and processing of data is safe and monitored. Where data is accessed by `Admins` assume that the school's policy is agreed by all staff who have access. Any user story item that requires this consideration has been flagged with a `security` tag.* 

| User Story Link | Requirement |
| ------------- | -------- |
| [#1]((https://github.com/NickdevC/Home-Learning-Hub/issues/1#issue-1562209793)) | I am able to access the landing page and easily access a login page link |
| [#2](https://github.com/NickdevC/Home-Learning-Hub/issues/2#issue-1562233203) | With a link from a `superuser`, I can access a signup page and register my details to create an account |
| [#3](https://github.com/NickdevC/Home-Learning-Hub/issues/4#issue-1562252150) | I am able to navigate to a login page where I can input my details and successfully login to the site |
| [#4](https://github.com/NickdevC/Home-Learning-Hub/issues/4#issue-1562252150) | On successfully logging in, I am redirected to the homepage where added accessibility is now visible on the nav bar |
| [#5](https://github.com/NickdevC/Home-Learning-Hub/issues/5#issue-1562258527) | I am able to logout of my account in order to maintain security on my system |
| [#6](https://github.com/NickdevC/Home-Learning-Hub/issues/5#issue-1562258527) | I am presented with a modal message to add an extra level of defensive programming. I must confirm my logout process before being returned to the landing page |
| [#7](https://github.com/NickdevC/Home-Learning-Hub/issues/23#issue-1574501441) | I can access an 'Appointments' page, where all booked appointments are displayed `security` |
| [#8](https://github.com/NickdevC/Home-Learning-Hub/issues/7#issue-1562279581) | I can edit individual appointment bookings, changing any of the fields entered by the user `security` |
| [#9](https://github.com/NickdevC/Home-Learning-Hub/issues/8#issue-1562284295) | I can permanently delete individual appointment bookings from the 'Appointments' page |
| [#10](https://github.com/NickdevC/Home-Learning-Hub/issues/8#issue-1562284295) | On selecting to delete an appointment booking, I am faced with an added layer of defensive programming and must confirm the process through a modal popup message |
| [#11]() | 


### Specific `Super Admin` Access

| User Story Link | Requirement |
| ----------- | -------- |
| [#1](https://github.com/NickdevC/Home-Learning-Hub/issues/13#issue-1562306829) | I can view all *booked appointments*, am able to edit these entries, and can use the data to monitor trends |
| [#2](https://github.com/NickdevC/Home-Learning-Hub/issues/35#issue-1599969836) | I can view all *uploaded reosurces*, am able to edit these entries, and can use the data to monitor trends |

### Developer Tasks 
Here I have documented some of the tasks I created as part of my agile approach to development. These tasks helped to fulfill the user stories listed above and demonstrate how the process was constant dialogue between the user/admin's needs and the site's functionality in practise.

| Dev Task Link | Details |
| ----------- | ------- |
| [#1]() |
