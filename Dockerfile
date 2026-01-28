# Use lightweight nginx image
FROM nginx:alpine

# Remove default nginx content
RUN rm -rf /usr/share/nginx/html/*

# Copy our app to nginx
COPY index.html /usr/share/nginx/html/

# Expose port
EXPOSE 80
