# JobTrack

**Track Every Application. Land Your Next Opportunity.**

JobTrack is a full-stack job and internship application tracker built as a medium-complexity B.Tech semester project. It uses React + Vite + Tailwind CSS on the frontend and Node.js + Express + MongoDB + Mongoose on the backend.

## Features
- JWT authentication with bcrypt password hashing
- Responsive purple SaaS dashboard
- Application CRUD with search, filtering and sorting
- Status pipeline / Kanban board
- Resume PDF upload and management using Multer
- Dashboard analytics and charts
- Interview/deadline calendar view
- User profile management
- User-scoped data access
- Centralized backend error handling

## Stack
React, Vite, Tailwind CSS, React Router, Axios, Recharts, Node.js, Express, MongoDB, Mongoose, JWT, bcryptjs, Multer.

## Folder structure
```text
JobTrack/
├── client/
│   └── src/
│       ├── components/
│       ├── context/
│       ├── pages/
│       ├── services/
│       └── utils/
├── server/
│   ├── config/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   └── uploads/
├── README.md
└── package.json
```

## Setup
1. Install Node.js and MongoDB.
2. Copy `server/.env.example` to `server/.env` and set `MONGO_URI` and `JWT_SECRET`.
3. From the root run `npm install`, then `npm run install-all`.
4. Run `npm run dev`.
5. Open `http://localhost:5173`.

## API
### Auth
- POST `/api/auth/register`
- POST `/api/auth/login`
- GET `/api/auth/me`
### User
- GET `/api/users/profile`
- PUT `/api/users/profile`
### Jobs
- POST `/api/jobs`
- GET `/api/jobs`
- GET `/api/jobs/:id`
- PUT `/api/jobs/:id`
- DELETE `/api/jobs/:id`
### Resumes
- POST `/api/resumes`
- GET `/api/resumes`
- DELETE `/api/resumes/:id`
### Analytics
- GET `/api/analytics`

## Viva points
React calls REST endpoints with Axios. Express authenticates requests with JWT middleware. Controllers use the authenticated user's ID rather than trusting a client-supplied user ID. Mongoose models map application data to MongoDB collections. Multer handles PDF upload to the server's local `uploads` folder. Dashboard analytics are calculated from the user's application documents.

## Academic note
The project intentionally avoids microservices, Docker, Redis, GraphQL and other unnecessary infrastructure so the architecture remains understandable and demonstrable for a third-year full-stack lab.
