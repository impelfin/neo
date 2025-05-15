# Step 1 : Base Images
FROM node:16.20.0

# Step 2 : Package Install 
RUN apt -y update; apt -y upgrade; apt -y install vim git net-tools

# Step 3 : Specify a Working directory
WORKDIR /root

# Step 4 : Config file copy
COPY .bashrc .
COPY .exrc .
COPY hello.js .

# Step 5 : Install express
RUN npm init -y
RUN npm install express
RUN npm install -g nodemon

# Step 6 : Open port
EXPOSE 8000

# Step 7 : Execution Program
CMD ["nodemon","hello.js"]
