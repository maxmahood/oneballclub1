# One Ball Club — Website Preview V7

Deploy this folder or its ZIP to Netlify. All 64 venues have a dedicated locally bundled, venue-named fallback graphic.

## Screenshot behavior
Each venue attempts to load a screenshot of its official URL from the public WordPress mShots service (`s.wordpress.com/mshots/v1/`). This service is third-party, can rate-limit or fail, and may show an old page or refuse a website. If the screenshot fails or times out, the local branded venue preview is shown. **The local previews are NOT actual website screenshots.** Live screenshots were not captured or packaged because network DNS is unavailable in the build environment.

Images from websites are subject to their owners' rights. Review service terms and secure any required permissions before commercial use. For production reliability, replace remote thumbnails with authorized locally saved captures and set up a screenshot refresh process.

Ratings/comments remain browser-local. Prices are estimates, not live rates.
