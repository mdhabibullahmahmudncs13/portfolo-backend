# Connecting Svelte Frontend to Django Backend

This guide shows you how to connect your Svelte frontend to this Django portfolio backend API.

## Prerequisites

- Django backend deployed on PythonAnywhere (or running locally)
- Svelte frontend project set up
- Backend API URL (e.g., `https://yourusername.pythonanywhere.com`)

## Step 1: Install Axios (or use Fetch API)

### Option A: Using Axios (Recommended)

```bash
npm install axios
```

### Option B: Using native Fetch API
No installation needed - built into browsers.

## Step 2: Create API Service

Create a file `src/lib/api.js` in your Svelte project:

```javascript
import axios from 'axios';

// Base URL for your Django backend
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true, // For CORS with credentials
});

// API endpoints
export const portfolioAPI = {
  // Hero section
  getHero: () => api.get('/hero/'),
  
  // Skills
  getSkills: () => api.get('/skills/'),
  getSkill: (id) => api.get(`/skills/${id}/`),
  
  // Projects
  getProjects: () => api.get('/projects/'),
  getProject: (id) => api.get(`/projects/${id}/`),
  getFeaturedProjects: () => api.get('/projects/featured/'),
  
  // Experience
  getExperience: () => api.get('/experience/'),
  
  // Certifications
  getCertifications: () => api.get('/certifications/'),
  
  // Contact
  getContact: () => api.get('/contact/'),
  
  // Messages (Contact form)
  sendMessage: (data) => api.post('/messages/', data),
  
  // Blog
  getBlogPosts: () => api.get('/blog/'),
  getBlogPost: (slug) => api.get(`/blog/${slug}/`),
  
  // Extra-curricular activities
  getActivities: () => api.get('/activities/'),
};

export default api;
```

### Alternative: Using Fetch API

If you prefer Fetch instead of Axios, create `src/lib/api.js`:

```javascript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

async function fetchAPI(endpoint, options = {}) {
  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    credentials: 'include', // For CORS with credentials
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }

  return response.json();
}

export const portfolioAPI = {
  getHero: () => fetchAPI('/hero/'),
  getSkills: () => fetchAPI('/skills/'),
  getProjects: () => fetchAPI('/projects/'),
  getFeaturedProjects: () => fetchAPI('/projects/featured/'),
  getExperience: () => fetchAPI('/experience/'),
  getCertifications: () => fetchAPI('/certifications/'),
  getContact: () => fetchAPI('/contact/'),
  sendMessage: (data) => fetchAPI('/messages/', {
    method: 'POST',
    body: JSON.stringify(data),
  }),
  getBlogPosts: () => fetchAPI('/blog/'),
  getBlogPost: (slug) => fetchAPI(`/blog/${slug}/`),
  getActivities: () => fetchAPI('/activities/'),
};
```

## Step 3: Configure Environment Variables

Create `.env` file in your Svelte project root:

```env
# For local development
VITE_API_URL=http://localhost:8000/api

# For production (uncomment and update)
# VITE_API_URL=https://yourusername.pythonanywhere.com/api
```

Create `.env.production` for production builds:

```env
VITE_API_URL=https://yourusername.pythonanywhere.com/api
```

## Step 4: Use API in Svelte Components

### Example: Fetching Skills

```svelte
<script>
  import { onMount } from 'svelte';
  import { portfolioAPI } from '$lib/api';

  let skills = [];
  let loading = true;
  let error = null;

  onMount(async () => {
    try {
      const response = await portfolioAPI.getSkills();
      skills = response.data;
    } catch (err) {
      error = err.message;
      console.error('Error fetching skills:', err);
    } finally {
      loading = false;
    }
  });
</script>

{#if loading}
  <p>Loading skills...</p>
{:else if error}
  <p class="error">Error: {error}</p>
{:else}
  <div class="skills-grid">
    {#each skills as skill}
      <div class="skill-card">
        <img src={skill.icon_image} alt={skill.name} />
        <h3>{skill.name}</h3>
        <p>{skill.category}</p>
      </div>
    {/each}
  </div>
{/if}
```

### Example: Hero Section

```svelte
<script>
  import { onMount } from 'svelte';
  import { portfolioAPI } from '$lib/api';

  let hero = null;
  let loading = true;

  onMount(async () => {
    try {
      const response = await portfolioAPI.getHero();
      hero = response.data;
    } catch (err) {
      console.error('Error fetching hero:', err);
    } finally {
      loading = false;
    }
  });
</script>

{#if loading}
  <p>Loading...</p>
{:else if hero}
  <section class="hero">
    <img src={hero.profile_image} alt={hero.name} />
    <h1>{hero.name}</h1>
    <h2>{hero.tagline}</h2>
    <p>{hero.bio}</p>
    
    <div class="social-links">
      {#if hero.github_url}
        <a href={hero.github_url} target="_blank">GitHub</a>
      {/if}
      {#if hero.linkedin_url}
        <a href={hero.linkedin_url} target="_blank">LinkedIn</a>
      {/if}
      {#if hero.twitter_url}
        <a href={hero.twitter_url} target="_blank">Twitter</a>
      {/if}
    </div>
  </section>
{/if}
```

### Example: Contact Form

```svelte
<script>
  import { portfolioAPI } from '$lib/api';

  let formData = {
    name: '',
    email: '',
    subject: '',
    message: ''
  };
  let submitting = false;
  let success = false;
  let error = null;

  async function handleSubmit() {
    submitting = true;
    error = null;
    success = false;

    try {
      await portfolioAPI.sendMessage(formData);
      success = true;
      formData = { name: '', email: '', subject: '', message: '' };
    } catch (err) {
      error = 'Failed to send message. Please try again.';
      console.error('Error sending message:', err);
    } finally {
      submitting = false;
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input
    type="text"
    bind:value={formData.name}
    placeholder="Your Name"
    required
  />
  <input
    type="email"
    bind:value={formData.email}
    placeholder="Your Email"
    required
  />
  <input
    type="text"
    bind:value={formData.subject}
    placeholder="Subject"
    required
  />
  <textarea
    bind:value={formData.message}
    placeholder="Your Message"
    required
  ></textarea>

  <button type="submit" disabled={submitting}>
    {submitting ? 'Sending...' : 'Send Message'}
  </button>

  {#if success}
    <p class="success">Message sent successfully!</p>
  {/if}
  {#if error}
    <p class="error">{error}</p>
  {/if}
</form>
```

## Step 5: Using Svelte Stores (Optional but Recommended)

Create `src/lib/stores/portfolio.js` for better state management:

```javascript
import { writable } from 'svelte/store';
import { portfolioAPI } from '$lib/api';

function createPortfolioStore() {
  const { subscribe, set, update } = writable({
    hero: null,
    skills: [],
    projects: [],
    experience: [],
    certifications: [],
    contact: null,
    loading: false,
    error: null,
  });

  return {
    subscribe,
    fetchHero: async () => {
      update(state => ({ ...state, loading: true }));
      try {
        const response = await portfolioAPI.getHero();
        update(state => ({ ...state, hero: response.data, loading: false }));
      } catch (error) {
        update(state => ({ ...state, error: error.message, loading: false }));
      }
    },
    fetchSkills: async () => {
      try {
        const response = await portfolioAPI.getSkills();
        update(state => ({ ...state, skills: response.data }));
      } catch (error) {
        update(state => ({ ...state, error: error.message }));
      }
    },
    fetchProjects: async () => {
      try {
        const response = await portfolioAPI.getProjects();
        update(state => ({ ...state, projects: response.data }));
      } catch (error) {
        update(state => ({ ...state, error: error.message }));
      }
    },
    // Add more methods as needed
  };
}

export const portfolio = createPortfolioStore();
```

Then use in components:

```svelte
<script>
  import { onMount } from 'svelte';
  import { portfolio } from '$lib/stores/portfolio';

  onMount(() => {
    portfolio.fetchHero();
    portfolio.fetchSkills();
  });
</script>

{#if $portfolio.loading}
  <p>Loading...</p>
{:else if $portfolio.hero}
  <h1>{$portfolio.hero.name}</h1>
{/if}
```

## Step 6: Handle Media Files

Django serves media files from the `/media/` endpoint. To display images:

```svelte
<script>
  const API_BASE = import.meta.env.VITE_API_URL.replace('/api', '');
  
  let skill = {
    name: 'Python',
    icon_image: '/media/skills/icons/python.png'
  };
</script>

<!-- Full URL for images -->
<img src="{API_BASE}{skill.icon_image}" alt={skill.name} />

<!-- Or create a helper function -->
<script>
  function getMediaUrl(path) {
    const API_BASE = import.meta.env.VITE_API_URL.replace('/api', '');
    return `${API_BASE}${path}`;
  }
</script>

<img src={getMediaUrl(skill.icon_image)} alt={skill.name} />
```

## Step 7: CORS Configuration

Ensure your Django backend's `.env` includes your frontend URL:

```env
# On PythonAnywhere or production
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com,https://www.your-frontend-domain.com

# For local development, also include
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,https://your-frontend-domain.com
```

## Step 8: Build and Deploy Frontend

### For Vercel:

1. Add environment variable in Vercel dashboard:
   - `VITE_API_URL` = `https://yourusername.pythonanywhere.com/api`

2. Deploy:
   ```bash
   vercel --prod
   ```

### For Netlify:

1. Create `netlify.toml`:
   ```toml
   [build]
     command = "npm run build"
     publish = "build"

   [[redirects]]
     from = "/*"
     to = "/index.html"
     status = 200
   ```

2. Add environment variable in Netlify dashboard:
   - `VITE_API_URL` = `https://yourusername.pythonanywhere.com/api`

## Troubleshooting

### CORS Errors
- Check Django backend `.env` has your frontend domain in `CORS_ALLOWED_ORIGINS`
- Ensure `corsheaders` is installed and in `INSTALLED_APPS`
- Verify `CorsMiddleware` is first in `MIDDLEWARE`

### Images Not Loading
- Check media file path is correct
- Verify media files are uploaded to PythonAnywhere
- Check media file mappings in PythonAnywhere Web tab

### Empty Data / 404 Errors
- Check API URL is correct (includes `/api` at the end)
- Verify backend has data (check admin panel)
- Test API directly in browser: `https://yourusername.pythonanywhere.com/api/skills/`

### Authentication Issues
- For public endpoints, no authentication needed
- Contact form uses `AllowAny` permission
- Admin endpoints require JWT tokens

## API Response Structure

All endpoints return data in this format:

```json
// List endpoints (e.g., /api/skills/)
[
  {
    "id": 1,
    "name": "Python",
    "category": "Backend",
    "icon_image": "/media/skills/icons/python.png"
  }
]

// Single item endpoints (e.g., /api/hero/)
{
  "id": 1,
  "name": "Your Name",
  "tagline": "Full Stack Developer",
  "bio": "..."
}
```

## Complete Example App Structure

```
svelte-portfolio/
├── src/
│   ├── lib/
│   │   ├── api.js                 # API service
│   │   ├── stores/
│   │   │   └── portfolio.js       # Svelte stores
│   │   └── components/
│   │       ├── Hero.svelte
│   │       ├── Skills.svelte
│   │       ├── Projects.svelte
│   │       ├── Experience.svelte
│   │       ├── Contact.svelte
│   │       └── Blog.svelte
│   ├── routes/
│   │   ├── +page.svelte          # Home page
│   │   └── blog/
│   │       └── [slug]/
│   │           └── +page.svelte  # Blog post page
│   └── app.html
├── .env                           # Local environment
├── .env.production                # Production environment
└── package.json
```

## Next Steps

1. Test API endpoints locally
2. Implement each component one by one
3. Add loading states and error handling
4. Deploy frontend
5. Update CORS settings with production domain
6. Test production deployment

---

Your Svelte frontend should now be successfully connected to your Django backend! 🎉
