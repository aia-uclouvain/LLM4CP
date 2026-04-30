# 🚀 Deployment Guide - Hugging Face Spaces

This guide walks you through deploying CP-Model-Zoo to [Hugging Face Spaces](https://huggingface.co/spaces).

## Prerequisites

- ✅ A Hugging Face account ([Sign up here](https://huggingface.co/join))
- ✅ A Groq API key ([Get one here](https://console.groq.com/keys))
- ✅ Git and Git LFS installed
- ✅ Vector databases pre-generated locally

## Step-by-Step Deployment

### 1. Generate Vector Databases Locally

Before deploying, generate the vector databases to avoid timeouts during startup:

```bash
python run_indexing.py
```

This creates the `data/vector_dbs/` directory needed by the app. **Commit this to git** so it's available in your Space.

### 2. Create a New Space on Hugging Face

1. Go to [https://huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Fill in the form:
   - **Owner**: Your username or organization
   - **Space name**: e.g., `cp-model-zoo` (must be unique)
   - **License**: Choose one (e.g., MIT, Apache 2.0)
   - **SDK**: Select **Gradio**
   - **Visibility**: Public or Private
4. Click **"Create Space"**

### 3. Clone Your Space Repository

```bash
git clone https://huggingface.co/spaces/<your-username>/<your-space-name>
cd <your-space-name>
```

### 4. Copy Your Project Files

Copy all files from your CP-Model-Zoo repo to the cloned Space directory:

```bash
cp -r /path/to/LLM4CP/* .
```

Ensure you have:
- `app.py` (entry point)
- `requirements.txt` (dependencies)
- `data/vector_dbs/` (pre-generated databases)
- `app/` directory (application code)
- Other necessary files

### 5. Add Your Groq API Key as a Secret

In your Space's settings:

1. Navigate to **Settings** → **Secrets and variables**
2. Click **"New secret"**
3. Enter:
   - **Name**: `GROQ_API_KEY`
   - **Value**: Your Groq API key
4. Click **"Save"**

### 6. Configure Persistent Storage

⚠️ **Important**: Vector databases are large and need persistent storage:

1. Go to **Settings** → **Persistent Storage**
2. Enable it and allocate **at least 50GB** (recommended)
3. This ensures your `data/` directory persists across restarts

### 7. Push to Your Space

```bash
git add .
git commit -m "Initial CP-Model-Zoo deployment"
git push
```

The Space will automatically build and launch your app. Check the logs for any errors.

### 8. Verify Deployment

- Your app should be live at: `https://huggingface.co/spaces/<your-username>/<your-space-name>`
- Test the search functionality to ensure it works correctly
- Check the **Logs** tab if you encounter issues

## Troubleshooting

### Issue: "Index storage directory not found"

**Solution**: Pre-generate vector databases locally before deployment:
```bash
python run_indexing.py
git add data/vector_dbs/
git commit -m "Add pre-generated vector databases"
git push
```

### Issue: Out of Memory

**Solution**: Increase persistent storage and RAM allocation in Space settings.

### Issue: GROQ_API_KEY not recognized

**Solution**: 
1. Verify the secret is named exactly `GROQ_API_KEY` (case-sensitive)
2. Restart the Space after adding the secret
3. Check that you're using the correct API key from Groq

### Issue: Dependencies fail to install

**Solution**: Ensure `requirements.txt` is in the root directory and contains all dependencies.

## Advanced Configuration

### Modify the README Frontmatter

To customize how your Space appears on Hugging Face, add YAML frontmatter to your README.md:

```yaml
---
title: CP-Model-Zoo
description: Natural Language Query System for Constraint Programming Models
sdk: gradio
sdk_version: "5.0"
app_file: app.py
colorFrom: blue
colorTo: green
pinned: false
persistent_storage:
  enabled: true
  max_size: 50
---
```

### Environment Variables

Additional environment variables you can set:

```bash
HF_TOKEN=your_token          # For private model access
TOKENIZERS_PARALLELISM=false # Performance optimization (already set in app.py)
```

## Documentation Links

- [Hugging Face Spaces Docs](https://huggingface.co/docs/hub/spaces-overview)
- [Gradio on Spaces](https://huggingface.co/docs/hub/spaces-sdks)
- [Persistent Storage Guide](https://huggingface.co/docs/hub/spaces-persistent-storage)
- [Secrets Management](https://huggingface.co/docs/hub/spaces-secrets)

## Support

If you encounter issues:

1. Check the **Logs** tab in your Space
2. Review the [Spaces documentation](https://huggingface.co/docs/hub/spaces)
3. Post on the [Hugging Face Forums](https://discuss.huggingface.co/)

---

**Ready to deploy?** Follow the steps above and your CP-Model-Zoo will be live on Hugging Face Spaces! 🎉

