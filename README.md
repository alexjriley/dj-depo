# Project overview

[DJ Depo banner image]

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

[Screenshot of project boards on Github/Trello]



### Concept and wireframe

[Screenshot of wireframe using Figma]

For this project, I used Figma to create a front-end mockup of the site. 

In the design of my homepage, I have largely stuck to the original designs as well as making improvements to the overall style and layout.

It was important to limit too much ideation with this project, so that development of the front-end did not exhaust the time constraints.





### 

## Deployment notes: Cloudinary

This project uses Cloudinary for media storage in production. Before deploying, make sure one of the following is set in the environment:

- `CLOUDINARY_URL` (recommended) — e.g. `cloudinary://<api_key>:<api_secret>@<cloud_name>`
- or the three separate vars: `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`

If you need to run management commands (for example `collectstatic`) in CI without production secrets, you can opt-in to skipping the Cloudinary credentials check by setting:

```
SKIP_CLOUDINARY_CHECK=1
```

This skip is conservative: it must be explicitly enabled and is intended for CI or build jobs where media uploads are not performed. Skipping will emit a warning in the process output so the decision is visible in logs. Do not rely on skipping for normal production deployments — ensure credentials are present for the running application.
