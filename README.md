# Project overview

<img width="1185" height="1050" alt="Screenshot 2025-11-09 at 15 54 19" src="https://github.com/user-attachments/assets/a412426f-e1c7-466f-b4de-b4de8c256b01" />

DJ Depo is a full-stack web application built for for DJs and mix enthusiasts to to discover and upload their own DJ mixes. It facilitates community-orientated sharing of fresh music mixes curated by DJs. 

- Users of the site can register a username and upload their mp3 mix - which is added to the homepage discovery seciton for visitors to enjoy.

- The goal was to create a simplified solution for DJs to upload their mixes in a community setting, with future development plans to expand interactions including social sharing and comments.

- Success critieria for the application was to build a simplified, responsive and easy-to-use interface for users to seamlessly upload and share their musics onto the site.

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
7. Mix Tags or Genres:

### Project board

<sub>Github project board (complete)</sub><br><img width="1196" height="840" alt="Screenshot 2025-11-09 at 15 39 23" src="https://github.com/user-attachments/assets/46842883-85a3-41a0-8d75-eafda01f9bf8" />

### Agile methodology

As a development team of one, working agile was essential. I used Github Projects to track user story requirements and for sprints I used a separate Trello board.

This ensured I was able to meet the criteria for site functionality and keep a check on time constraints for the project as a whole.

The sprints ran for one week and focused on key areas of development

- Week 1 sprint: Backend setup and authentication (Django).
- Week 2 sprint: Javascript model and custom templates (HTML). 
- Week 3 sprint: Frontend design (CSS) and testing.

<sub>Trello sprint board (complete)</sub><br><img width="726" height="858" alt="Screenshot 2025-11-09 at 15 37 58" src="https://github.com/user-attachments/assets/5c6d2bcd-7815-4757-a3f4-1e87f5a012d5" />

## Design

### Concept and wireframe

For this project, I used Figma to create a wireframe and interactive front-end mockup of the site.  In the design of my homepage, I have largely stuck to the original designs as well as making improvements to the overall style and layout.

<sub>Wireframe</sub><br> ![website-app-wireframe](https://github.com/user-attachments/assets/b3e2af5c-6378-469b-9b79-db1a8bb10c94)

<sub>Figma mock-up</sub><br> ![dj-depo-figma](https://github.com/user-attachments/assets/817e1163-7780-40e2-8b45-9a19a785f6e7) <a href="https://www.figma.com/proto/6l3lN5EkOBqiOt3E1EZqwY/dj.depo?node-id=1-3908&scaling=min-zoom&content-scaling=fixed&t=R6DRqAfJW9GuPCEj-1"> Figma link </a>

## Development

### Database Development

<sub>Admin panel</sub><br> ![django-admin-panel](https://github.com/user-attachments/assets/d34b482d-22ef-4a3d-a8a0-c29f812a76de)

After creating a remote repository, I set up the Django environment ready to use the Model View Template Framework.

I then connected a Postgre database to make the application functional and enable the creation of an admin panel, users and begin to develop CRUD functionality.

### Custom Model

<sub>Mix model</sub><br> ![audio-post-model](https://github.com/user-attachments/assets/b0aae2f4-7793-4e59-90e0-f829426f2680)

The main componenet of the DJ Depo app is this AudioPost model, with custom elements to enhance UX.

Enables users to:

- Upload audio posts associated with their accounts.
- Store a title, description and an audio file.
- Integrates with Cloudinary for storage in the cloud.
- Bypasses Cloudinary during tests and stores files locally.
- Records timestamp for uploads. 

#### Database patch

The AudioPost model in /mix/models.py explicitly sets the database table name to hello_world_audiopost. 

This is because hello_world app was the original location of the model, and it was later moved to mixes. Despite the move, the database table name remains `hello_world_audiopost` to maintain compatibility with existing data.

See documentation in mixes/models.py for further clarification.

## Deploying the project locally

### Cloudinary

This project uses Cloudinary for media storage in production. Before deploying, make sure one of the following is set in the environment:

- `CLOUDINARY_URL` (recommended) — e.g. `cloudinary://<api_key>:<api_secret>@<cloud_name>`
- or the three separate vars: `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`

If you need to run management commands (for example `collectstatic`) in CI without production secrets, you can opt-in to skipping the Cloudinary credentials check by setting:

```
SKIP_CLOUDINARY_CHECK=1
```

This skip is conservative: it must be explicitly enabled and is intended for CI or build jobs where media uploads are not performed. Skipping will emit a warning in the process output so the decision is visible in logs. Do not rely on skipping for normal production deployments — ensure credentials are present for the running application.
