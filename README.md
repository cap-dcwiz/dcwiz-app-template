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

## Deployment

1. populate the `.env` file with the correct values.
to be continued...

2. Run the following command to start the server.
```bash
pr ansible-playbook -i ansible/hosts.yaml -e host_group=experimental ansible/up.yaml
```

3. Run the following command to stop the server.
```bash
pr ansible-playbook -i ansible/hosts.yaml -e host_group=experimental ansible/down.yaml
```

4. Run the following command to clean.
```bash
pr ansible-playbook -i ansible/hosts.yaml -e host_group=experimental ansible/clean.yaml
```
