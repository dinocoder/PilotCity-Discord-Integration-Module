FROM node:12.18.2
WORKDIR /usr/src/app
RUN yarn global add @vue/cli
COPY package*.json ./
RUN yarn install
COPY . .
EXPOSE 8080

CMD [ "yarn", "run", "serve" ]