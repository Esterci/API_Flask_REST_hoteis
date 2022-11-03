FROM node

WORKDIR /app

#ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./

RUN npm install -g @vue/cli

RUN npm i --save

RUN npm audit fix

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]