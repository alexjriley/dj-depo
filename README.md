# DJ Depo

<p align="center">
  <a href="https://dj-depo-a90b7064471a.herokuapp.com/" target="_blank">
  <img width="800" height="1024" alt="dj-depo-banner" src="https://github.com/user-attachments/assets/8fd353f3-c920-421c-af04-f851716d46c4" />
    </a>
</p>

<p align="center"><em>A full-stack Django web app for DJs to share and discover new mixes.
</em></p>

## Contents

- [Tech Stack](#tech-stack)  
- [Project Overview](#project-overview)
- [User Guide](#user-guide)  
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
  - [Unit tests](#unit-tests)
  - [Accessibility](#accessibility)
  - [Validation](#validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)  
  - [Responsive Screen Tests](#responsive-screen-tests)  
- [Use of AI Tools](#use-of-ai-tools)
  - [Strategic use](#strategic-use)
  - [Debugging](#debugging)
  - [Optimising code](#optimising-code)
  - [Unit test generation](#unit-test-generation)
  - [Documentation](#documentation)   
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

## User Guide

### Sign up

To register for an account, click signup and enter a username and password.

<p align="center">
  <img width="400" alt="App signup" src="https://github.com/user-attachments/assets/dea2f173-2862-49ed-963f-32babfcc9984"/>
</p>

### Login

If you are not logged in automatically, navigate to the login page and enter the details you used to signup.

<p align="center">
  <img width="400" alt="App Login page" src="https://github.com/user-attachments/assets/0fa6d10c-0c31-4150-baf9-72ef5884fe4c"/>
</p>

### Upload

Once your account is created, you can login and share uploads to the homepage. Click upload a mix to navigate to the upload page.

<p align="center">
  <img width="400" alt="Mix upload page" src="https://github.com/user-attachments/assets/0523783f-3876-4e1a-9533-1ebd691f0587"/>
</p>

Add a title, description and audio file then click upload. If successful, you should be redirected to the homepage and see this message.

<p align="center">
  <img width="400" alt="Success message" src="https://github.com/user-attachments/assets/076c873f-aa87-4b0b-bf09-b378ce179a29"/>
</p>

#### Important note on uploading files

DJ Depo is still in production and currently it cannot support large files. 

If you are testing the site, please find a demo MP3 track to upload <a href="https://drive.google.com/drive/folders/198uLGmtQAayjhMTstJl2PxTFeRQPT6cj?usp=drive_link" target="_blank"> here </a>.

### Edit or delete

Made a mistake? No problem, you can choose to edit or delete your upload from the homepage.

<p align="center">
  <img width="400" alt="Edit or delete" src="https://github.com/user-attachments/assets/13916e88-59ae-48ac-a7ab-eaafce0da4cf"/>
</p>

<p align="center">
  <img width="400" alt="Edit upload" src="https://github.com/user-attachments/assets/2d8aa3ca-4fd7-43bc-a5ee-5b68e8bcb504"/>
</p>

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
  <img width="600" alt="Github project board" src="https://github.com/user-attachments/assets/46842883-85a3-41a0-8d75-eafda01f9bf8"/>
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
  <img width="600" alt="Trello project board" src="https://github.com/user-attachments/assets/5c6d2bcd-7815-4757-a3f4-1e87f5a012d5" />
</p>

<p align="center"><em>Trello sprint board</em></p>

## Design

### Concept and wireframe

For this project, I used Figma to create a wireframe and interactive front-end mockup of the site.  In the design of my homepage, I have largely stuck to the original designs as well as making improvements to the overall style and layout.

<p align="center">
  <img width="600" alt="Wireframed" src="https://github.com/user-attachments/assets/5281e399-bea5-425a-8db2-c0c6b1ed2534"/>
</p>

<p align="center"><em>Wireframe</em></p>


<p align="center">
  <a href="https://www.figma.com/proto/6l3lN5EkOBqiOt3E1EZqwY/dj.depo?node-id=1-3908&scaling=min-zoom&content-scaling=fixed&t=R6DRqAfJW9GuPCEj-1" target="_blank">
  <img width="600" alt="Figma front-end mockup" src="https://github.com/user-attachments/assets/817e1163-7780-40e2-8b45-9a19a785f6e7"/>
    </a>
</p>

<p align="center"><em>Figma mock-up — click image to open</em></p>

## Development

### Database Development

<p align="center">
  <img width="600" alt="Admin panel" src="https://github.com/user-attachments/assets/225200c3-9b66-4f9d-a827-ff279716279d"/>
</p>

<p align="center"><em>Admin panel</em></p>

After creating a remote repository, I set up the Django environment ready to use the Model View Template Framework.

I then connected a PostgreSQL database to make the application functional and enable the creation of an admin panel, users and begin to develop CRUD functionality.

### Custom Model

<p align="center">
  <img width="600" alt="Code snippet for a custom model" src="https://github.com/user-attachments/assets/b0aae2f4-7793-4e59-90e0-f829426f2680"/>
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

### Unit tests

The mixes app includes a comprehensive suite of unit tests to ensure the functionality and reliability of its models, views, and workflows. These tests cover:

- Model Tests: Validation of the AudioPost model, including its creation and string representation.
- View Tests: Verification of view accessibility, login requirements, and CRUD operations for audio posts.
- Integration Tests: End-to-end testing of workflows, such as creating, editing, and deleting audio posts.
- Error Handling Tests: Validation of 404 errors and form submission error handling.

All tests were executed successfully on 10 November 2025, with the following results:

| Test Suite | Result |
| ------------- | ------------- |
| AudioPostModelTest  | Ok  |
| HomePageViewTest  | Ok  |
| UploadAudioViewTest  |  Ok  |
| EditPostViewTest  | Ok  |
| DeleteAudioPostViewTest  | Ok  |
| IntegrationTests  | Ok  |
| ErrorHandlingTests  | Ok  |

Total Tests: 12
Passed: 12
Failed: 0

To run your own tests in development use the command:

`python3 manage.py test mixes` or 
`python manage.py test mixes` depending on your device.

<p align="center">
  <img width="600" alt="Running tests in terminal" src="https://github.com/user-attachments/assets/39501034-43a7-4bd6-b6f2-9be90912f78a"/>
</p>

<p align="center"><em>Unit tests</em></p>

### Accessibility

Lighthouse report score (Google Dev Tools)

| Performance  | Accessibility | Best Practices |
| ------------- | ------------- | ------------- |
| 73  | 100  | 100  |


<p align="center">
  <img width="600" alt="Lighthouse test score" src="https://github.com/user-attachments/assets/0b002b72-ddb3-42b0-b4d2-34f2bcd33ed1"/>
</p>

<p align="center"><em>Lighthouse score</em></p>

### Validation

#### HTML 

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

#### CSS

CSS Validation Service (W3C)

| CSS  | Validator pass/fail |
| ------------- | ------------- |
| `static>style.css`  | PASS  |

#### JavaScript

jshint.com

`mixes/static/mixes/js/wavesurfer-init.js`

| Metric | Value | Notes |
|--------|--------|-------|
| Total functions | 14 | — |
| Max function parameters | 2 | Median: 0.5 |
| Max statements per function | 18 | Median: 10.5 |
| Max cyclomatic complexity | 8 | Median: 4 |


#### Python

CI Python Linter (Pep8)

| File  | Validator pass/fail | Screenshot
| ------------- | ------------- | ------------- |
| `mixes>admin.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/8a041bf5-cbfb-4b31-81a5-67f7df3c5268" width="300" alt="Lint test result for admin.py" /></p> |
| `mixes>apps.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/b6105da4-a4e0-4326-839b-73ce77724d8a" width="300" alt="Lint test result for apps.py" /></p> |
| `mixes>forms.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/5cfeb6ba-afac-40a5-a9c3-e05062855fa7" width="300" alt="Lint test result for forms.py" /></p> |
| `mixes>models.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/ac765ee7-dc4c-4fd9-8f09-8381a60013fe" width="300" alt="Lint test result for models.py" /></p> |
| `mixes>tests.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/e4436b81-ff75-4fb8-8887-e323f2b9ae52" width="300" alt="Lint test result for tests.py" /></p> |
| `mixes>urls.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/6e87edd5-62f8-45d7-aa5a-cd83c4b353c2" width="300" alt="Lint test result for mixes.py" /></p> |
| `mixes>views.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/137a0d87-73a8-4b97-a2df-0e1f144f7f29" width="300" alt="Lint test result for views.py" /></p> |
| `config>settings.py`  | PASS  | <p align="center"><img src="https://github.com/user-attachments/assets/2a8e7747-57dd-4f3b-83f9-8af5d6b7989e" width="300" alt="Lint test result for settings.py" /></p> |

### Responsive Screen Tests

| Device  | Mockup | Notes
| ------------- | ------------- | ------------- |
| Small device (iPhone SE) | <p align="center"><img src="https://github.com/user-attachments/assets/d39a26ab-1015-4b72-9fea-3c3a88d135bc" width="300" alt="iPhone SE layout test" /></p> | Menu collapses to hamburger; audio player fits screen width; homepage layout remains usable. |
| Medium device (iPad Pro 11) | <p align="center"><img src="https://github.com/user-attachments/assets/57680b1c-f70f-43f2-b037-bdc94347fdf3" width="350" alt="iPad Pro 11 layout test" /></p> | Audio player scales correctly, mixes display in grid view |
| Large device (Macbook Pro 13) | <p align="center"><img src="https://github.com/user-attachments/assets/ea9b45ba-6db2-4f8e-83cc-98850db395d7" width="400" alt="MacBook Pro 13 layout test" /></p> | Full desktop layout with 3 mixes per row |


## Use of AI tools



### Strategic use

Throughout this project, I leveraged Microsoft Co-Pilot’s AI agent integration in VS Code to enhance productivity, support decision-making, and improve code quality. Key areas where AI contributed include:

- Error troubleshooting: Diagnosing HTTP errors (e.g., 400, 500) and suggesting actionable solutions.
- Feature customisation: Assisting with Django model adjustments and JavaScript waveform integration.
- Code review: Providing feedback on accessibility, maintainability, and overall code quality.

### Debugging

AI played a pivotal role in debugging, helping me overcome blockers efficiently while also providing learning opportunities. For example, when customising the Wavesurfer.js plugin—a critical component of the front-end UX—the default progress bar obstructed the waveform. Using Co-Pilot, I was able to understand the underlying issue and implement a workaround (applying a drop-shadow instead of a solid shape).

Although the solution was not perfect, AI enabled me to extend the project’s functionality beyond my immediate JavaScript expertise, accelerating development while reinforcing my problem-solving skills.

### Optimising code

Co-Pilot was also instrumental in ensuring visual and functional consistency. For instance, I used AI to apply Bootstrap styling across modals so that interactions like editing or deleting posts matched the design of login and signup templates. This allowed me to make rapid, coherent updates that maintained a polished front-end UX.

### Unit Test Generation

Finally, AI assisted in creating Django unit tests, which proved invaluable for debugging and verifying application functionality. Co-Pilot helped automate repetitive testing tasks, allowing me to focus on higher-level logic and ensuring the app worked reliably.

### Documentation

AI assistance was essential in maximising time for development by producing documentation including structuring and improving readme., generating concise inline code descriptions, responding to project ideas and assisting with planning and providing user stories ready to implement into the project board.

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
