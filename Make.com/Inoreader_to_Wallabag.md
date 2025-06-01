# 📥 Inoreader to Wallabag Integration (Make.com Scenario)

This Make.com scenario automates the process of saving articles tagged "Keep" in **Inoreader** directly into your **Wallabag** instance for long-term reading and archiving. I built this because Pocket is shutting down and I wanted to replace Pocket with Wallabag then I realized that Inoreader does not natively support sharing to Wallabag, so I used Make.com to bridge them 

## 🚀 Overview

Whenever you tag an article with **"Keep"** in Inoreader, this automation will:
1. **Watch for newly tagged articles** via Inoreader.
2. **Request an OAuth2 token** from Wallabag using a password-based grant.
3. **Send the article URL** to Wallabag’s API to be saved to your reading list.

## 🔧 Requirements

Before importing or using this scenario, ensure the following:

- An active **Inoreader** account with articles tagged "Keep".
- A **Wallabag** instance (self-hosted or hosted) with API access enabled.
- Wallabag OAuth2 credentials:
  - `client_id`
  - `client_secret`
  - `username`
  - `password`

## 🧩 Scenario Modules

| Step | Module | Description |
|------|--------|-------------|
| 1 | **Inoreader - Watch Articles** | Monitors the Inoreader label/tag `Keep` for new articles. |
| 2 | **HTTP - Get OAuth Token** | Authenticates with Wallabag using OAuth2 and retrieves a bearer token. |
| 3 | **HTTP - Save to Wallabag** | Sends the article URL from Inoreader to Wallabag using the token. |

## ⚙️ Customization

### Replace placeholders in the HTTP modules:
- `WALLABAG_URL` → Your Wallabag instance domain (e.g., `https://app.wallabag.it`)
- `CLIENT_ID`, `CLIENT_SECRET`, `USERNAME`, `PASSWORD` → Your OAuth credentials

In the second HTTP module, the body should look like:
```plaintext
grant_type=password&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&username=USERNAME&password=PASSWORD
```

In the third HTTP module, the request body:
```json
{
  "url": "{{4.canonical[].href}}"
}
```

Make sure the Authorization header includes:
```http
Authorization: Bearer {{5.data.access_token}}
```

## 📦 Importing the Scenario

To use this scenario:
1. Download the `.json` file.
2. Open [Make.com](https://www.make.com).
3. Go to `Scenarios` → `Create new scenario` → `Import Blueprint`.
4. Upload the JSON file and connect your Inoreader and Wallabag accounts.

## 🙌 Credits

Developed using [Make.com](https://make.com) -- At the time of writing, Make.com offers a free plan with up to 1000 actions / month
