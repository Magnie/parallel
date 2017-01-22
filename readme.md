# Lessons Learned
When I first worked on this I was trying to learn Django and also implement a concept my coworker had told me. That was separating the frontend from the backend and using API calls to send and receive data. So I started developing it and after a week or so I realized what my mistake was. I was trying to use Django's templates to create pages and pass some basic session data in. The lesson I learned from this project was that you shouldn't be using template systems for backend servers or even use backend servers to serve frontend content.

# Install
1. Create django project
2. Drag and drop 'forum' app into project.
3. Add static settings to settings.py

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```

# Extending Parallel
Please follow these consistency rules:
* 4 spaces per tab.
* Scripts go under the HTML it directly responds to.
* Anything that retrieves or submits data should be an AJAX call.
* No hardcoded URLs. Use {% url %}.
* If views get too big, split it into "partials" and include them (makes for easier reusability too!).
