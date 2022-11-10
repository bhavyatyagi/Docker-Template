# syntax=docker/dockerfile:1

# build on alpine linux with node's latest stable verion
FROM node:lts-alpine

# change cwd
WORKDIR /react-app

# node_modules and serve
COPY ./package*.json .
RUN npm install --quiet
RUN npm install -g serve

# copy code
COPY . .

# create production build
RUN npm run build

EXPOSE 3000
CMD [ "serve", "-s", "build", "-p", "3000"]