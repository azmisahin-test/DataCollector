FROM node:14

WORKDIR /app
COPY src/ ./
COPY package.json ./
RUN npm install

CMD ["node", "app.js"]
