# Install
1. Create django project
2. Drag and drop 'forum' app into project.
3. Add static settings to settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Extending Parallel
Please follow the consistency rules.
4 spaces per tab.
Scripts go under the HTML it directly responds to.
Anything that retrieves or submits data should be an AJAX call.
No hardcoded URLs. Use {% url %}.
If views get too big, split it into "partials" and include them (makes for easier reusability too!).
