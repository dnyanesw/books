DOCKER_COMPOSE_FILE=docker-compose.yml
if [ -f "$DOCKER_COMPOSE_FILE" ]; then
    if [ "$1" = "staging" ]; then
        git checkout dev || { echo 'git checkout failed' ; exit 1; }
        git pull origin dev  || { echo 'git pull failed' ; exit 1; }
    elif [ "$1" = "prod" ]; then
        git checkout master || { echo 'git checkout failed' ; exit 1; }
        git pull origin master || { echo 'git pull failed' ; exit 1; }
    else
        echo "Unknown environment"
        exit 1
    fi
    docker-compose -f $DOCKER_COMPOSE_FILE build
    docker-compose -f $DOCKER_COMPOSE_FILE down
    docker-compose -f $DOCKER_COMPOSE_FILE up -d
    docker-compose -f $DOCKER_COMPOSE_FILE exec flask pipenv run flask db upgrade heads
else
    echo "$FILE docker-compose file not exists."
fi
