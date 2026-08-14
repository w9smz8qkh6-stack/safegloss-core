# Vendor-neutral deployment

SafeGloss Core is a WSGI Django application backed by PostgreSQL. The included Dockerfile runs Gunicorn as an unprivileged user and serves collected static assets through WhiteNoise.

## Required production configuration

- `DJANGO_SECRET_KEY`: a long random value stored in a secret manager;
- `DATABASE_URL`: a PostgreSQL connection URL;
- `ALLOWED_HOSTS`: comma-separated public hostnames;
- `DEBUG=False`; and
- TLS termination at the reverse proxy or platform edge.

Set `SECURE_SSL_REDIRECT=True` after proxy headers and HTTPS behavior have been verified. Enable HSTS subdomains and preload only when every affected hostname is permanently HTTPS-capable.

## Release sequence

1. Back up the PostgreSQL database.
2. Build an immutable image from a reviewed tag.
3. Run `python manage.py check --deploy` with production configuration.
4. Run `python manage.py migrate --noinput` as a one-off release task.
5. Start the web process.
6. Confirm `/health/`, login, and an authorized glossary view.

Do not run migrations independently from every replica during a rolling deployment.

## Persistent data

PostgreSQL is the only persistent service in the first public core. Back it up using the operator's normal PostgreSQL tools and test restores regularly. The project does not ship a production backup scheduler.

## Rollback

Application rollback means redeploying the prior image. Database rollback depends on the migrations in the release; review each migration before deployment and retain a tested backup when a migration is not safely reversible.
