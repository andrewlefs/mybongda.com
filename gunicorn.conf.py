import multiprocessing

# Server Socket
bind = 'unix:/tmp/gunicorn.sock'
backlog = 2048

# Worker
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 30
keepalive = 2
debug = True
spew = False

# Logging
logfile = '/var/log/gunicorn/log'
loglevel = 'info'
logconfig = None

# Process Name
proc_name = 'gunicorn_myball'
