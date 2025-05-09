# Step 1
FROM node:16

# Step 2
WORKDIR /usr/src/app

# Step 3
RUN git clone https://github.com/impelfin/docker-publish
WORKDIR /usr/src/app/docker-publish/st_info
RUN npm install

# Step 4
EXPOSE 8080

# Step 5
CMD ["node","app.js"]