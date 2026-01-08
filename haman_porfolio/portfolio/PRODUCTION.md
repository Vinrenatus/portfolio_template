# Production Deployment Guide

## Backend Setup

### Environment Variables
Create a `.env` file in the backend directory with the following variables:

```env
FLASK_ENV=production
SECRET_KEY=your-super-secret-production-key-here
DATABASE_URL=postgresql://username:password@localhost/dbname
SMTP_SERVER=smtp.your-email-provider.com
SMTP_PORT=587
SMTP_USERNAME=your-email@domain.com
SMTP_PASSWORD=your-app-password
```

### Running with Gunicorn
```bash
cd portfolio/backend
source venv/bin/activate
pip install -r requirements_prod.txt
gunicorn --config gunicorn.conf.py run:app
```

### Running with Docker
```bash
cd portfolio
docker-compose up -d
```

## Frontend Setup

### Environment Variables
Create a `.env.production` file in the frontend directory:

```env
REACT_APP_API_URL=https://yourdomain.com/api
REACT_APP_ENVIRONMENT=production
```

### Building for Production
```bash
cd portfolio/frontend
npm install
npm run build
```

## Deployment Options

### Option 1: Manual Deployment
1. Deploy the backend to your server
2. Deploy the frontend build to a static hosting service (Netlify, Vercel, etc.)
3. Configure your domain and SSL certificates

### Option 2: Containerized Deployment
1. Build and deploy using Docker Compose
2. Configure reverse proxy (nginx) if needed
3. Set up SSL certificates

### Option 3: Cloud Platforms
- **Heroku**: Use the Procfile to deploy
- **AWS**: Use ECS or Elastic Beanstalk
- **Google Cloud**: Use App Engine or GKE
- **Azure**: Use App Service or AKS

## Security Best Practices

1. **Never commit secrets to version control**
2. **Use HTTPS in production**
3. **Set proper CORS policies**
4. **Implement rate limiting**
5. **Use strong passwords and API keys**
6. **Regular security updates**

## Performance Optimizations

1. **Enable Gzip compression**
2. **Use a CDN for static assets**
3. **Implement caching strategies**
4. **Optimize database queries**
5. **Minimize bundle sizes**

## Monitoring & Logging

1. **Set up error tracking (Sentry)**
2. **Monitor application performance**
3. **Log important events**
4. **Set up health checks**
5. **Configure alerts**

## Backup Strategy

1. **Regular database backups**
2. **Version control for code**
3. **Configuration management**
4. **Disaster recovery plan**

## Maintenance

1. **Regular updates**
2. **Security patches**
3. **Performance monitoring**
4. **Log rotation**
5. **Database maintenance**

## Troubleshooting

### Common Issues
- CORS errors: Check ALLOWED_ORIGINS in backend
- Database connection: Verify DATABASE_URL
- Static files: Ensure proper build and serving
- SSL certificates: Use proper certificate chain

### Logs Location
- Backend: `/var/log/portfolio/backend.log`
- Frontend: Browser console and server logs
- Database: `/var/lib/postgresql/data/pg_log/`

### Health Checks
- Backend: `GET /api/health`
- Frontend: `GET /health`
- Database: Connection test

## Scaling

### Horizontal Scaling
- Use load balancer
- Scale backend instances
- Use external database
- Implement session management

### Vertical Scaling
- Increase server resources
- Optimize database performance
- Improve caching strategies
- Monitor resource usage