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
RUN npm install express

# Step 5 : Open port
EXPOSE 8000

# Step 6 : Execution Program
CMD ["node","hello.js"]
