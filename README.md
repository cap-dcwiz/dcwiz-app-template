# dcwiz-app-template
Cookiecutter Template of DCWiz Applications

## Usage

Run the following command and follow the prompts to generate a new project.
```bash
$ cookiecutter gh:cap-dcwiz/dcwiz-app-template
```

## Development

1. The database models should be placed in the `{project_slug}/db/models` folder.
2. The database operations should be placed in the `{project_slug}/db/data` folder.
3. The API endpoints should be placed in the `{project_slug}/api` folder.
4. Each subfolder in the `{project_slug}/api` folder will be a independent API router.
5. Put the API schemas in the `{project_slug}/api/schemas` folder.
6. Put the API endpoints in the `{project_slug}/api/router` folder.
7. The endpoints under "default" router will be mounted to the root path.
8. The endpoints under other routers will be mounted to the path of the router.
9. After deployment, by default, the API will be available at `http://<host>:<port>/<APP_PATH>`, which is set during 
the initialization of the project. If you want to change the path, modify the docker compose file.

### How to setup the development environment

1. Install [poetry](https://python-poetry.org/docs/#installation).

2. Install poetry environment and dependencies.
```bash
$ poetry install
```

3. If database is needed, create the database and user.
```bash
$ docker compose up -d
```
Note: the docker-compose.yaml file will be created only when the database is needed.

4. Create a .env file
```bash
$ cp export/env.dev .env
```

5. Run the following command to start the service.
```bash
$ poetry run <app name>
```
Note: Check the `pyproject.toml` file to see the name of the app. By default, it is the project folder name but 
replacing "_" with "-".

6. Check the API documentation at `http://localhost:8000/docs`. By default, there should be a health check endpoint.

#### Database init and migration
If the app uses database, run the following command to init, migrate or upgrade tables.
```bash
DCWIZ_APP_CONFIG=config/config.toml poetry run alembic revision --autogenerate
DCWIZ_APP_CONFIG=config/config.toml poetry run alembic upgrade head
```

<!-- Deployment is now deprecated in favor of dcwiz-projects centralised development -->
<!--
## Deployment

Note: all the commands should be run in poetry virtual environment.

### 1. populate the `.env` and authorization files.
```bash
ansible-playbook \
  -i ansible/hosts.yaml \
  -e host_group=test \
  -e env_file=export/env.example \
  ansible/up.yaml
```
Note: if env_file is not specified, ".env" will be used by default.

### 2. Build docker images
```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --push \
  -t ghcr.io/cap-dcwiz/<image_name>:test \
  .
```
where, by default, the image name is the project folder name, and the tag is the host group name.

Note: you may need to login to the container registry first.

### 3. Run the following command to start the service.
```bash
ansible-playbook \
  -i ansible/hosts.yaml \
  -e host_group=test \
  ansible/up.yaml
```

### 4. Run the following command to stop the service.
```bash
ansible-playbook \
  -i ansible/hosts.yaml \
  -e host_group=test \
  ansible/down.yaml
```

### 5. Run the following command to stop the service and clean.
```bash
ansible-playbook \
  -i ansible/hosts.yaml \
  -e host_group=test \
  ansible/clean.yaml
```
Note: this command will remove all the data in the database, as well as populated `.env` and authorization files.

### How to enable github actions

1. ADD `SSH_PRIVATE_KEY` in the repository secrets.
2. Repo settings => Actions => General => Enable "Read and write permissions" 
3. Package settings => Manage Action access => add repo -->
