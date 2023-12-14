# Portfolio Datenbanken

- [Requirements](./docs/requirements.md)
- [Data](./docs/yelpData.md)

## Setup

### 1. Build
```bash
docker-compose up -d --build
```

### 2. Update
```bash
docker-compose up
```

### 3. Initial Import Mongo
- Execute index.py in operations/initialImports
```bash
import mongo
```