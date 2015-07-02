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
Scripts go under HTML.
Most "get" functions should use AJAX.
No hardcoded URLs. Use {% url %}.
