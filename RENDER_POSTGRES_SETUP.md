# 🐘 PostgreSQL Setup on Render

Upgrade from SQLite to PostgreSQL for persistent data storage.

## 🚀 Quick Setup (5 minutes)

### Step 1: Create PostgreSQL Database
1. In Render dashboard, click **"New Database"**
2. Choose **PostgreSQL**
3. Name: `seo-generator-db`
4. Free tier: **90 days free**
5. Click **"Create Database"**

### Step 2: Get Database URL
After creation, copy the **Internal Database URL**:
```
postgresql://user:password@hostname:port/database
```

### Step 3: Update Environment Variables
In your web service settings, update:
```env
DATABASE_URL=postgresql://user:password@hostname:port/database
```

### Step 4: Install PostgreSQL Driver
Add to `requirements.txt`:
```txt
# Add this line
psycopg2-binary==2.9.7
```

### Step 5: Deploy
```bash
git add requirements.txt
git commit -m "Add PostgreSQL support"
git push
```

## 🔄 Data Migration (Optional)

If you have existing SQLite data to migrate:

```python
# migration_script.py
import sqlite3
import psycopg2
import json
import os

# Connect to SQLite
sqlite_conn = sqlite3.connect('seo_generator.db')
sqlite_cursor = sqlite_conn.cursor()

# Connect to PostgreSQL
pg_conn = psycopg2.connect(os.getenv('DATABASE_URL'))
pg_cursor = pg_conn.cursor()

# Migrate products
sqlite_cursor.execute("SELECT * FROM products")
products = sqlite_cursor.fetchall()

for product in products:
    pg_cursor.execute("""
        INSERT INTO products (id, slug, name, category, features, keywords, 
                            location, target_audience, seo_title, meta_description,
                            intro_content, sections, faqs, call_to_action, 
                            json_ld_schema, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, product)

pg_conn.commit()
print("✅ Migration complete!")
```

## 🎯 Benefits of PostgreSQL

- **Persistent Data**: Never lose your products
- **Better Performance**: Handles more concurrent users
- **Full-Text Search**: Better search capabilities
- **JSON Support**: Perfect for your features/keywords columns
- **Backup & Recovery**: Automated backups

## 💡 Alternative: Keep SQLite + Manual Backups

If you prefer to keep SQLite:

1. **Export data regularly:**
```bash
# Download your SQLite file from Render
curl https://your-app.onrender.com/backup > backup.db
```

2. **Store backups in GitHub:**
```bash
git add backup.db
git commit -m "Database backup $(date)"
git push
```

## 🤔 Which Should You Choose?

**Use PostgreSQL if:**
- You want persistent data
- Planning to scale
- Want production features

**Keep SQLite if:**
- Simple setup preferred
- Small-scale usage
- Don't mind occasional data resets

**My recommendation: Go with PostgreSQL** - the 90-day free trial gives you plenty of time to see if Render works for you! 🎯 