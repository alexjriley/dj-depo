# dj-depo
Capstone project repository for a DJ set depository.

## Project overview

For this capstone project, I decided on an audio focused website for users who are DJs and looking for quality DJ mixes.

Making use of the full stack skills learned on the course, I was able to 

- Create an upload audio model which allows users to upload audio files, with a title and description.
- Add CRUD functionality on the front-end, allowing users to edit or delete their authored posts.
- Use a mixture of Bootstrap and CSS to create a contemporary front-end with responsive design across devices.

### User stories

To speed up development time, I asked Chat GPT to generate a set of user stories based on a description of the project.

1. User Registration & Login: As a DJ, I want to create an account and log in so that I can securely upload and manage my mixes.
2. 

### Project planing

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
