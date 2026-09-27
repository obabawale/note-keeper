# Note Keeper FastAPI Application
This is an application that keeps notes (more like todo list) for a specific user.

### Todo

- [ ] Add unit test for both the models and api
- [ ] Add celery
- [ ] Add seed.py file for data seeding
- [ ] Add note api inside api package
- [ ] Dockerize the application

### In Progress

- [ ] Initialize database with superuser
- [ ] Create script to run at startup for creating superuser

### Done ✓

- [x] Add user model
- [x] Add note model
- [x] Create the project and run fastapi with uvicorn
- [x] Create a skeletal project structure
- [x] Create database connection
- [x] Add alembic for migration
- [x] Create configuration for Alembic, postgresql database
- [x] Add user schema with pydantic data validator
- [x] Add note schema with pydantic schema validator
- [x] Add base crud class
- [x] Add crud operation for user class
- [x] Create crud operation for note class
- [x] Add functions to hash user password and verify user password at login
- [x] Add functions to create user token for CORS apps