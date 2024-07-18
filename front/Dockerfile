FROM node:20.11.1 as build
WORKDIR /frontPrueba
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build
EXPOSE 5173
CMD [ "npm","run","serve"]