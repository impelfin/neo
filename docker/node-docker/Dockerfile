# Step 1:
FROM node:16

# Step 2:
WORKDIR /usr/src/app

# Step 3:
COPY package*.json .
RUN npm install

# Step 4:
COPY server.js .

# Step 5:
EXPOSE 8000

# Step 6:
CMD ["node","server.js"]
