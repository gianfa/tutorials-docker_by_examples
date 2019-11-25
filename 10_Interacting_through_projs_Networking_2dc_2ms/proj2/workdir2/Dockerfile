FROM node:10
#create app directory
WORKDIR  /home/node/app/
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /home/node/app/
COPY index.js /home/node/app/
RUN yarn install
CMD [ "node", "server.js" ]