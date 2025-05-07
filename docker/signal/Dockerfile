# Base Images
FROM iojs:latest

# Action
COPY ./sig_test.js .
COPY ./package.json .

# Port
EXPOSE 8000

# Exec
ENTRYPOINT ["node", "sig_test"]