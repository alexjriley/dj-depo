# DJ Depo

<p align="center">
  <a href="https://dj-depo-a90b7064471a.herokuapp.com/" target="_blank">
  <img width="800" alt="Github project board" src="https://github.com/user-attachments/assets/a412426f-e1c7-466f-b4de-b4de8c256b01"/>
    </a>
</p>

A full-stack Django web app for DJs to share and discover new mixes.

## Contents

- [Tech Stack](#tech-stack)  
- [Project Overview](#project-overview)  
- [Planning](#planning)  
  - [User Stories](#user-stories)  
  - [Project Board](#project-board)  
  - [Agile Methodology](#agile-methodology)  
- [Design](#design)  
  - [Concept and Wireframe](#concept-and-wireframe)  
- [Development](#development)  
  - [Database Development](#database-development)  
  - [Custom Model](#custom-model)  
- [Testing](#testing)  
  - [Accessibility](#accessibility)  
  - [Responsive Screen Tests](#responsive-screen-tests)  
- [Use of AI Tools](#use-of-ai-tools)  
- [Getting Started](#getting-started)  
  - [Deploying the Project Locally](#deploying-the-project-locally)  
- [Future Development](#future-development)

## Tech stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)

## Project overview

DJ Depo is a full-stack web application built for DJs and mix enthusiasts to discover and upload their own DJ mixes. It facilitates community-orientated sharing of fresh music mixes curated by DJs. 

- Users of the site can register a username and upload their mp3 mix - which is added to the homepage discovery section for visitors to enjoy.

- The goal was to create a simplified solution for DJs to upload their mixes in a community setting, with future development plans to expand interactions including social sharing and comments.

- Success criteria for the application were to build a simplified, responsive and easy-to-use interface for users to seamlessly upload and share their music onto the site.

- Where similar websites have a focus on the user, DJ Depo is focused on building the community of users and a shared ethos to create a platform with an ever-expanding collection of DJ mixes for users to access and enjoy.

## Planning

### User stories

To speed up development time, I asked Chat GPT to generate a set of user stories based on a description of the project.

1. User Registration & Login: As a DJ, I want to create an account and log in so that I can securely upload and manage my mixes.
2. Uploading a Mix: As a site user, I want to upload my mix file along with its title, date, and description so that listeners can discover and play my latest work.
3. CRUD functionality (front-end): As a site user, I want to edit the title, description or file, or delete an upload entirely.
4. Discover Mixes: As a site visitor, I want to browse a list of the most recent mixes so that I can find new music and discover different DJs.
5. Play Mixes: As a visitor, I want to listen to a mix directly from the website using an audio player so that I don’t need to download files to hear them.
6. Responsive Design: As a user, I want to navigate and play mixes easily on my phone, tablet or large screen devices.
7. Mix Tags or Genres: As a DJ, I want to add tags or select a genre for each mix so that listeners can easily filter and discover mixes by style.

### Project board

<p align="center">
  <a href="https://github.com/users/alexjriley/projects/8" target="_blank">
  <img width="800" alt="Github project board" src="https://github.com/user-attachments/assets/46842883-85a3-41a0-8d75-eafda01f9bf8"/>
    </a>
</p>

<p align="center"><em>Github project board — click image to open</em></p>

### Agile methodology

As a development team of one, working agile was essential. I used Github Projects to track user story requirements and for sprints I used a separate Trello board.

This ensured I was able to meet the criteria for site functionality and keep a check on time constraints for the project as a whole.

The sprints ran for one week and focused on key areas of development

- Week 1 sprint: Backend setup and authentication (Django).
- Week 2 sprint: JavaScript model and custom templates (HTML). 
- Week 3 sprint: Frontend design (CSS) and testing.

<p align="center">
  <img width="800" alt="Trello project board" src="https://github.com/user-attachments/assets/5c6d2bcd-7815-4757-a3f4-1e87f5a012d5" />
</p>

<p align="center"><em>Trello sprint board</em></p>

## Design

### Concept and wireframe

For this project, I used Figma to create a wireframe and interactive front-end mockup of the site.  In the design of my homepage, I have largely stuck to the original designs as well as making improvements to the overall style and layout.

<p align="center">
  <a href="https://www.figma.com/proto/6l3lN5EkOBqiOt3E1EZqwY/dj.depo?node-id=1-3908&scaling=min-zoom&content-scaling=fixed&t=R6DRqAfJW9GuPCEj-1" target="_blank">
  <img width="800" alt="Github project board" src="https://github.com/user-attachments/assets/817e1163-7780-40e2-8b45-9a19a785f6e7"/>
    </a>
</p>

<p align="center"><em>Figma mock-up — click image to open</em></p>

## Development

### Database Development

<p align="center">
  <img width="800" alt="Admin panel" src="https://github.com/user-attachments/assets/225200c3-9b66-4f9d-a827-ff279716279d"/>
</p>

<p align="center"><em>Admin panel</em></p>

After creating a remote repository, I set up the Django environment ready to use the Model View Template Framework.

I then connected a PostgreSQL database to make the application functional and enable the creation of an admin panel, users and begin to develop CRUD functionality.

### Custom Model

<p align="center">
  <img width="800" alt="Code snippet for a custom model" src="https://github.com/user-attachments/assets/b0aae2f4-7793-4e59-90e0-f829426f2680"/>
</p>

<p align="center"><em>Custom mix model</em></p>

The main component of the DJ Depo app is this AudioPost model, with custom elements to enhance UX.

Enables users to:

- Upload audio posts associated with their accounts.
- Store a title, description and an audio file.
- Integrates with Cloudinary for storage in the cloud.
- Bypasses Cloudinary during tests and stores files locally.
- Records timestamp for uploads.

#### Database patch

The AudioPost model in /mix/models.py explicitly sets the database table name to hello_world_audiopost. 

This is because the hello_world app was the original location of the model, and it was later moved to mixes. 

Despite the move, the database table name remains `hello_world_audiopost` to maintain compatibility with existing data.

This change does not affect the functionality of the application, as Django seamlessly handles the mapping between the model and the database table.

## Testing

### Accessibility

Lighthouse report score (Google Dev Tools)

| Performance  | Accessibility | Best Practices |
| ------------- | ------------- | ------------- |
| 73  | 100  | 100  |


<p align="center">
  <img width="800" alt="Lighthouse test score" src="https://github.com/user-attachments/assets/0b002b72-ddb3-42b0-b4d2-34f2bcd33ed1"/>
</p>

<p align="center"><em>Lighthouse score</em></p>

Markup Validation Service HTML (W3C)

| HTML  | Validator pass/fail |
| ------------- | ------------- |
| `templates>base.html`  | PASS  |
| `templates>registration>login.html` | PASS  |
| `templates>registration>signup.html` | PASS  |
| `templates>registration>signup.html` | PASS  |
| `mixes>templates>mixes>signup.html>edit_audio_post.html` | PASS  |
| `mixes>templates>mixes>signup.html>home.html` | PASS  |
| `mixes>templates>mixes>signup.html>post_confirm_delete.html` | PASS  |
| `mixes>templates>mixes>signup.html>upload_audio.html` | PASS  |

CSS Validation Service (W3C)

| CSS  | Validator pass/fail |
| ------------- | ------------- |
| `static>style.css`  | PASS  |


### Pep8 (Pylint extension VS Code)

| File  | Validator pass/fail |
| ------------- | ------------- |
| `mixes>admin.py`  | PASS  |
| `mixes>apps.py`  | PASS  |
| `mixes>forms.py`  | PASS  |
| `mixes>models.py`  | PASS  |
| `mixes>tests.py`  | PASS  |
| `mixes>urls.py`  | PASS  |
| `mixes>views.py`  | PASS  |

### Responsive Screen Tests

| Device  | Mockup | Notes
| ------------- | ------------- | ------------- |
| Small device (iPhone SE) | <p align="center"><img src="https://github.com/user-attachments/assets/d39a26ab-1015-4b72-9fea-3c3a88d135bc" width="300" alt="iPhone SE layout test" /></p> | Menu collapses to hamburger; audio player fits screen width; homepage layout remains usable. |
| Medium device (iPad Pro 11) | <p align="center"><img src="https://github.com/user-attachments/assets/57680b1c-f70f-43f2-b037-bdc94347fdf3" width="350" alt="iPad Pro 11 layout test" /></p> | Audio player scales correctly, mixes display in grid view |
| Large device (Macbook Pro 13) | <p align="center"><img src="https://github.com/user-attachments/assets/ea9b45ba-6db2-4f8e-83cc-98850db395d7" width="400" alt="MacBook Pro 13 layout test" /></p> | Full desktop layout with 3 mixes per row |


## Use of AI tools

### Strategic use

In this project, I used Microsoft Co-Pilot's AI agent integration in VS Code to provide support on areas such as:

- Troubleshooting errors (500, 400) and suggesting solutions
- Assisting in customising Django model and JavaScript waveform
- Reviewing the project for accessibility and code quality

### Debugging

On more than one occasion, I used AI to support debugging issues. This avoided using up time on blockers and I used each opportunity to learn from the assistant so that I could approach the problem myself in the future.

One example of this was customisation of the Wavesurfer.js plugin. This was a crucial component of the front-end UX for the application, however the out of the box version didn't match the clean front-end UX of the site.

I used the Copilot agent to understand why the progress bar was obstructing the waveform. Although the solution (using a drop-shadow as opposed to a solid shape) was short of perfect, this was an example where AI assistance enabled the project to be elevated beyond my JavaScript abilities.

### Optimising code

Another area where AI was beneficial was in making style adjustments using Bootstrap.

I was able to ask CoPilot to use Bootstrap styling to ensure modals had a consistent feel with the front-end.

For example, when implementing modals to pop-up when users edit or delete posts, I asked Copilot to match the styling with the templates used on the login and signup templates, meaning I could make swift and consistent changes to bring all forms, templates and modals into visual consistency.

### Create unit tests for Django

I used Copilot to create several tests to ensure the app was working correctly.

This was especially useful when debugging.

## Getting started

`git clone <repo>
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver`

### Deploying the project locally

### Cloudinary

This project uses Cloudinary for media storage in production. Before deploying, make sure one of the following is set in the environment:

- `CLOUDINARY_URL` (recommended) — e.g. `cloudinary://<api_key>:<api_secret>@<cloud_name>`
- or the three separate vars: `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`

If you need to run management commands (for example `collectstatic`) in CI without production secrets, you can opt-in to skipping the Cloudinary credentials check by setting:

```
SKIP_CLOUDINARY_CHECK=1
```

This skip is conservative: it must be explicitly enabled and is intended for CI or build jobs where media uploads are not performed. Skipping will emit a warning in the process output so the decision is visible in logs. Do not rely on skipping for normal production deployments — ensure credentials are present for the running application.

## Future Development

### Upcoming goals 

Looking ahead, I plan to introduce more social-based functionality including comments, ratings, and shared playlists along with the genre tags and search function that I ran out of time to implement in this project.

Furthermore, I would improve the branding from its basic, minimal theme to something more energetic and unique. Moving away from the Bootstrap heavy layout and implementing a different, more kinetic framework such as React.
