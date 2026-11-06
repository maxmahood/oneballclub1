# One Ball Club: automated venue website screenshots

This project includes a GitHub Actions workflow that opens all 64 official business URLs in Chromium, captures a 1440x900 screenshot of each homepage, and commits successful JPG images to `screenshots/`. The site already checks for these local files first.

## One-time setup
1. Create a GitHub repository and upload **the contents of this folder**, including the hidden `.github` directory. The simplest approach is to unzip locally and run `git init`, `git add .`, `git commit -m "Initial site"`, then push to your new repository. Alternatively use GitHub's upload files interface, ensuring `.github/workflows/capture-previews.yml` is included.
2. In GitHub, open **Actions** > **Capture venue website previews** > **Run workflow**.
3. In repository Settings > Actions > General > Workflow permissions, enable **Read and write permissions** so the action can commit the JPG files. Organization policies may override this.
4. Open the workflow run and inspect `screenshots/report.json` or the downloadable report artifact. Any failed URLs need an alternate source or a manually approved image. A successful screenshot can still be a cookie wall or blocked-page screenshot, so visually review captures before launch.
5. Download the repository ZIP after the workflow finishes and deploy the site contents to Netlify, or connect the GitHub repository to Netlify for automatic deployments on commit.

The workflow also attempts a monthly refresh. Some websites prohibit automation or reuse of their content; check their terms and permissions before publishing commercial screenshots. No screenshots are included in this initial ZIP, because they have not been captured. The existing venue-labeled fallback graphics remain in place for unsuccessful captures.
