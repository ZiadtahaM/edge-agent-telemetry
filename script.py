import os
import subprocess

def write_file(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

write_file('package.json', '''{
  "name": "agent-visibility-templatewww",
  "version": "1.0.0",
  "main": "src/index.js",
  "scripts": {
    "dev": "wrangler dev",
    "deploy": "wrangler deploy"
  },
  "devDependencies": {
    "wrangler": "^3.0.0"
  }
}''')

write_file('wrangler.toml', '''name = "agent-visibility-templatewww"
main = "src/index.js"
compatibility_date = "2024-02-22"

[env.staging]
name = "agent-visibility-templatewww-staging"
vars = { ENVIRONMENT = "staging" }

[env.production]
name = "agent-visibility-templatewww-production"
vars = { ENVIRONMENT = "production" }
''')

write_file('src/index.js', '''export default {
  async fetch(request, env, ctx) {
    const environment = env.ENVIRONMENT || 'development';
    return new Response(JSON.stringify({ message: "Hello from companion worker", environment }), {
      headers: { "content-type": "application/json" }
    });
  }
};
''')

write_file('README.md', '''# Agent Visibility Template WWW

Companion Cloudflare Worker with multi-environment configuration.

## What it does
This repository houses the companion worker for the agent visibility system. It features a staging and production split using wrangler environments. The worker returns environment-specific responses for multi-environment deployments.

## Tech
- Cloudflare Workers
- JavaScript

## Architecture
`mermaid
flowchart TD
    Request --> Worker
    Worker --> Staging(Staging Env)
    Worker --> Production(Production Env)
`

## Getting started
`ash
npm install
npm run dev
npm run deploy -- --env staging
`
''')
