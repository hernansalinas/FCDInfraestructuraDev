import pwd, subprocess, os
#from nbgitpuller_link import Link
#import nbgitpuller as nbp
#import nbgitpuller as nbp
#import nbgitpuller_link as nblink

"""
Libreria necesaria para generar el path 
de nbgitpuller, en el localhost
"""

def generate_link(url, repo, branch, subpath=""):
    pull_git = "/hub/user-redirect/git-pull?repo="
    branch_ = f"&branch={branch}"
    subPath_ = f"&subPath={subpath}"
    app="&app=lab"

    if(len(subpath))!=0:
      url_valida=f"{url}{pull_git}{repo}{branch_}{subPath_}"
    else:
      url_valida=f"{url}{pull_git}{repo}{branch_}{app}"
    return url_valida

c = get_config()  # noqa: F821


admin = os.environ.get("JUPYTERHUB_ADMIN")
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.Authenticator.admin_users = {"JUPYTERHUB_ADMIN"}
c.Authenticator.admin_users = ["admin"]

#c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
#c.Authenticator.admin_users = {'admin'}
#c.NativeAuthenticator.minimum_password_length = 8
#c.NativeAuthenticator.check_common_password = True
#c.NativeAuthenticator.allowed_failed_logins = 5
#c.NativeAuthenticator.seconds_before_next_try = 600
def pre_spawn_hook(spawner):
    username = spawner.user.name
    
    try:
        pwd.getpwnam(username)
       # subprocess.run(['nbgitpuller', 'http://localhost:8000/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fhernansalinas%2FFundCienDatosMaterial_year_semestre_dev&urlpath=tree%2FFundCienDatosMaterial_year_semestre_dev%2F&branch=main'])
    except KeyError:
        subprocess.check_call(['useradd', '-ms', '/bin/bash', username])        
        # Creando directorios iniciales para cada estudiante
        #subprocess.run(['mkdir', f'/home/{username}/Proyectos'])
        #subprocess.run(['mkdir', f'/home/{username}/Tareas'])
        #subprocess.run(['mkdir', f'/home/{username}/Laboratorios'])        
        #subprocess.run(['mkdir', f'/home/{username}/Material'])
        msg = f"Hola {username} bienvenid@ al curso de fundamentos en ciencia de datos de la universidad de Antioquia"
        subprocess.run(['echo', f'{msg}', '>', 'readme.txt'])
        #subprocess.run(['nbgitpuller', 'http://localhost:8000/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fhernansalinas%2FFundCienDatosMaterial_year_semestre_dev&urlpath=tree%2FFundCienDatosMaterial_year_semestre_dev%2F&branch=main'])
        #Crear directorios iniciales para el estudiante
        # Se debe tener un sistema para no crear usuarios infinitamente y generar 
        # caidas del sistemas, siempre se debe revisar si el usuairo est
        # Si se crea un nuevo usuario y no esta en la lista no lo carga
        # El usuario debe estar en la lista.


url = "http://localhost:8000"
repo= "https://github.com/hernansalinas/FundCienDatosMaterial_year_semestre_dev"
branch = "main" # La rama del repositorio de Git
launch_path = "/hw/hw01/hw01.ipynb"
#nbgitpuller_url = generate_link(url, repo, branch, launch_path)
nbgitpuller_url = generate_link(url, repo, branch)

c.JupyterHub.default_url=nbgitpuller_url 


c.Spawner.pre_spawn_hook = pre_spawn_hook
#c.Spawner.default_url = '/jupyterhub'

notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jupyterhub/work")
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}




# Roles de usuarios
#c.JupyterHub.load_roles = True
#c.JupyterHub.roles_config_file = '/srv/jupyterhub/permisos.json'

#  {
#         'name': 'administrador',
#         'description': 'Un rol para los usuarios que solo pueden acceder a sus propios servidores y recursos',
#         'scopes': ['inherit'],
#         'users': ['admin'],
#         'groups': ['administrador']
#     },
# Pasar los nombres de los usuarios y generar contrasenas aleatorias
# enviar contrasena aleatoria al usuario por correo electrinico

c.JupyterHub.load_roles = [   
    {
        'name': 'estudiante',
        'description': 'Un rol para los usuarios que solo pueden\
              acceder a sus propios servidores y recursos',
        'scopes': ['self'],
        'users': ['bob','fernando','gloria','verde','cyan','ernesto','mono'],
        'groups': ['estudiantes']
    },
    {
        'name': 'instructor',
        'description': 'Un rol para los usuarios que pueden acceder a\
              los servidores y recursos de los estudiantes',
        'scopes': ['read:users!group=estudiantes', 'access:servers!group=estudiantes'],
        'users': ['pedro', 'juan' ,'bosco', 'laura'],
        'groups': ['instructores']
    }
]

c.Authenticator.allowed_users = {'bob','fernando','gloria','verde','cyan',\
                                 'pedro', 'juan' ,'bosco', 'laura', 'ernesto','mono','tar'}



c.JupyterHub.load_groups = {
    'administrador': ['admin'],
    'estudiantes': ['bob', 'fernando','gloria', 'laura','verde','cyan'],
    'instructores': ['pedro','juan' ,'bosco']
}



#subprocess.run(['jupyterhub', 'upgrade-db'])
# Los usuarios pueden ser creados con contrasenas aleatorias

# c.JupyterHub.load_roles =   [{
#     'name': 'pedro',
#     'description': 'Allows parties to start and stop user servers',
#     'scopes': ['servers'],
#     'users': ['alice', 'bob'],
#     'services': ['idle-culler'],
#     'groups': ['admin-group'],
#     }]
# [
#     {
#         "name": "pedro",
#         "description": "Regular user with access to their own server",
#         "scopes": ["self", "read:users"],
#         "users": [],
#         "groups": [],
#         "services": [],
#     },
#     {
#         "name": "juan",
#         "description": "Admin user with full access to the API",
#         "scopes": ["inherit"],
#         "users": ["admin1"],
#         "groups": [],
#         "services": [],
#     }, 
#    
# ]

# # Copyright (c) Jupyter Development Team.
# # Distributed under the terms of the Modified BSD License.

# # Configuration file for JupyterHub
# import os

# c = get_config()  # noqa: F821

# # We rely on environment variables to configure JupyterHub so that we
# # avoid having to rebuild the JupyterHub container every time we change a
# # configuration parameter.

# # Spawn single-user servers as Docker containers
# c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# # Spawn containers from this image
# c.DockerSpawner.image = os.environ["DOCKER_NOTEBOOK_IMAGE"]

# # Connect containers to this Docker network
# network_name = os.environ["DOCKER_NETWORK_NAME"]
# c.DockerSpawner.use_internal_ip = True
# c.DockerSpawner.network_name = network_name

# # Explicitly set notebook directory because we'll be mounting a volume to it.
# # Most `jupyter/docker-stacks` *-notebook images run the Notebook server as
# # user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# # We follow the same convention.
# notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jupyterhub/work")
# c.DockerSpawner.notebook_dir = notebook_dir

# # Mount the real user's Docker volume on the host to the notebook user's
# # notebook directory in the container
# c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}

# # Remove containers once they are stopped
# c.DockerSpawner.remove = True

# # For debugging arguments passed to spawned containers
# c.DockerSpawner.debug = True

# # User containers will access hub by container name on the Docker network
# c.JupyterHub.hub_ip = "jupyterhub"
# #c.JupyterHub.hub_port = 8000

# # Persist hub data on volume mounted inside container
# c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
# c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

# # Authenticate users with Native Authenticator
# c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

# # Allow anyone to sign-up without approval
# c.NativeAuthenticator.open_signup = True

# # Allowed admins
# admin = os.environ.get("JUPYTERHUB_ADMIN")
# if admin:
#     c.Authenticator.admin_users = [admin]
