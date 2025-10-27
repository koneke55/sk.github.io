# GitHub Hosting Guide for Your Portfolio

## Quick Start Guide

Follow these steps to host your portfolio on GitHub Pages.

### Step 1: Update Configuration

Update the following in `_config.yml`:

**Line 19-20:** Replace with your GitHub username and repository name
```yaml
url: https://YOUR-GITHUB-USERNAME.github.io
baseurl: /YOUR-REPOSITORY-NAME
```

For example, if your GitHub username is `samboukone` and repository is `portfolio`:
```yaml
url: https://samboukone.github.io
baseurl: /portfolio
```

**IMPORTANT:** If you want to host at `https://YOUR-USERNAME.github.io` (without subpath), leave `baseurl` empty:
```yaml
url: https://samboukone.github.io
baseurl:  # (leave blank or just put nothing)
```

### Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository name: `portfolio` or `sambou-kone-portfolio` (or any name you like)
4. Choose **Public** (GitHub Pages is free for public repos)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **"Create repository"**

### Step 3: Push Your Code to GitHub

Run these commands in PowerShell (in this directory):

```powershell
# Add all files
git add .

# Commit the changes
git commit -m "Initial commit: Portfolio setup"

# Add your GitHub repository as remote (replace YOUR-USERNAME and YOUR-REPO-NAME)
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Rename branch to main (GitHub uses 'main' by default)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right of the repository)
3. Scroll down to **Pages** (in the left sidebar)
4. Under **Source**, select **"GitHub Actions"**
5. The site will deploy automatically!

### Step 5: Wait for Deployment

1. Go to **Actions** tab in your repository
2. Watch the "Deploy site" workflow run (takes about 2-4 minutes)
3. Once it's complete, your site will be live at:
   - `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME` (if you set a baseurl)
   - `https://YOUR-USERNAME.github.io` (if you left baseurl empty)

### Step 6: Update Social Links (Optional)

In `_data/socials.yml`, you can uncomment and add your social media profiles:
```yaml
linkedin_username: # your LinkedIn username
github_username: # your GitHub username
research_gate_profile: # your ResearchGate profile
```

## Important Notes

### Repository Name Options

**Option A: Personal Site (Recommended)**
- Create repository named `YOUR-USERNAME.github.io`
- Set `baseurl: ` (empty) in `_config.yml`
- Site URL: `https://YOUR-USERNAME.github.io`

**Option B: Project Site**
- Create repository named anything (e.g., `portfolio`)
- Set `baseurl: /portfolio` in `_config.yml`
- Site URL: `https://YOUR-USERNAME.github.io/portfolio`

### Custom Domain (Optional)

If you have a custom domain:
1. Update `url` in `_config.yml` to your domain
2. Add a file named `CNAME` in the root directory with just your domain name
3. Configure DNS settings with your domain provider

## Troubleshooting

### Deployment fails in GitHub Actions
- Check if `_config.yml` has correct URLs
- Ensure all files are committed
- Check the Actions tab for error messages

### Site shows old content
- Hard refresh the browser (Ctrl+F5)
- Wait a few minutes for changes to propagate
- Check if deployment workflow completed successfully

### Need help?
- Check the Actions tab for build logs
- See [GitHub Pages documentation](https://docs.github.com/en/pages)
- Check [al-folio FAQ](FAQ.md)

## Next Steps

1. **Add a profile picture**: Put your photo as `assets/img/prof_pic.jpg`
2. **Update projects**: Edit files in `_projects/` folder
3. **Add blog posts**: Write posts in `_posts/` folder
4. **Update social links**: Complete `_data/socials.yml`

Your portfolio will auto-deploy every time you push changes to GitHub! 🚀
