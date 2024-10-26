FROM node:20

WORKDIR /app
COPY src/ ./
COPY package.json ./
RUN npm install

CMD ["node", "app.js"]
