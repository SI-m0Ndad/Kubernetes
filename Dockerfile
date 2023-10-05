# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install API dependencies
RUN npm install

# Copy your API source code to the container
COPY . .

# Expose the API port
EXPOSE 30000

# Start the API when the container starts
CMD ["node", "app.js"]
